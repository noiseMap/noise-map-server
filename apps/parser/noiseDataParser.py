#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import pandas
import argparse
from pyproj import Proj

from apps.common.djangoUtil import setup_django, database_copy
setup_django()
from django.db import connection


class NoiseDataParser(object):
    
    ERT_FILE_EXTENSION = ".ERT"
    ERT_FILE_SEPERATOR = "\s+"
    ERT_FILE_COLUMNS = ["latitude", "longitude", "noise_mean_day", "noise_mean_night", "elevation", "noise_mean_evening", "noise_weighted_24h", "noise_mean_24h"]
    
    def __init__(self):
        pass
        
    def run(self, data_dir):
        ert_files = [file for file in os.listdir(data_dir) if file.endswith(self.ERT_FILE_EXTENSION)]
        
        frames = []
        for filename in ert_files:
            frames.append( self.read_file( os.path.join(data_dir, filename) ) )
            
        dataFrame = frames[0]
        for f in frames[1:]:
            dataFrame = dataFrame.append(f, ignore_index=True)
            
        #self.preprocessing(df)
        self.store(dataFrame, filename=os.path.join(data_dir, "data.csv"))

    def read_file(self, filename):
        """Reads a single ERT CSV file"""
        return pandas.read_csv(filename, skiprows=4, skipfooter=1, sep=self.ERT_FILE_SEPERATOR, names=self.ERT_FILE_COLUMNS, index_col=False, engine="python")
    
    def preprocessing(self, df):
        # Convert longitude and latitude
        hhProj = Proj("+proj=utm +zone=32N, +ellps=WGS84 +datum=WGS84 +units=m +no_defs")
        lon, lat = hhProj(df['latitude_raw'].values*1000, df['longitude_raw'].values*1000, inverse=True)
        df["longitude"] = pandas.Series(lon)
        df["latitude"] = pandas.Series(lat)
    
    def store(self, dataFrame, filename):
        """Store the data in the database.

        First we store the data in a CSV file. Then we can use a
        bulk import to import the complete CSV file into the
        PostgreSQL database. The code is not the prettiest but
        fast.
        """
        columns = ["longitude", "latitude", "elevation", "noise_mean_day", "noise_mean_evening", "noise_mean_night", "noise_weighted_24h", "noise_mean_24h"]
        self.store_in_csv(dataFrame, filename=filename, columns=columns)

        columns.insert(0, "id") # pandas adds a id in the front
        self.store_in_database(filename=filename, columns=columns)

    def store_in_csv(self, dataFrame, filename, columns, sep="\t", encoding="utf-8"):
        dataFrame.to_csv(filename, sep=sep, encoding=encoding, columns=columns, header=False, index=True)

    def store_in_database(self, filename, columns):
        # TODO: Remove the hard coded table name
        with connection.cursor() as cursor:
            database_copy(cursor, filename=filename, table="noisedata_noisedata", columns=columns)


def parse_args():
    parser = argparse.ArgumentParser(description='''Parses a noise data set''')
    parser.add_argument('data_dir', help='Data directory with the *.ert files')
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    
    parser = NoiseDataParser()
    parser.run(data_dir=args.data_dir)
