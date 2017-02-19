#!/usr/bin/python
# -*- coding: utf-8 -*-

def setup_django():
    """Setup Django for using the app in a script."""
    import django
    from apps.server import wsgi  # Defines the settings
    django.setup()

def database_copy(cursor, filename, table, columns):
    """Copy CSV file into PostgreSQL database.
        
    @see: http://initd.org/psycopg/docs/cursor.html
    :param cursor: Database cursor
    :param filename: Name of the CSV file
    :param table: Database table name
    :param columns: Table columns
    :return: If copy was successful
    """
    import logging
    from psycopg2._psycopg import ProgrammingError, OperationalError, DataError,\
        InternalError  
    try:
        # This is a specific feature of PostgreSQL
        cursor.copy_from(file=open(filename, 'r'), table=table, sep='\t')
        return True
    except(DataError, InternalError, ProgrammingError, OperationalError) as e: # by psycopg2
        logging.warn(e, exc_info=True)
    except(IOError) as e: # by open(<file>)
        logging.warn(e, exc_info=True)
    return False
