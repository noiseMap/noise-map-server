from django.contrib.gis.db import models

class NoiseData(models.Model):
    #center = models.PointField(null=True)
    # Redundant to center (for faster import)
    latitude = models.FloatField()
    longitude = models.FloatField()

    elevation = models.FloatField()
    #bounding_box = models.GeometryField()
    # TODO: PostGIS supports RasterField, which we could use instead of GeometryField.

    noise_mean_day = models.FloatField()
    noise_mean_evening = models.FloatField()
    noise_mean_night = models.FloatField()
    noise_weighted_24h = models.FloatField()
    noise_mean_24h = models.FloatField()

    def __unicode__(self):
        return unicode('NoiseDate ({},{}) {}'.format(self.latitude, self.longitude, self.noise_mean_24h))


class Dummy(models.Model):
    name = models.CharField(max_length=150)
    position = models.FloatField()
    
    point = models.PointField(dim=3, null=True)

    def latitude(self):
        return self.point.y

    def longitude(self):
        return self.point.x

    # Output name in admin interface
    def __unicode__(self):
        return unicode(self.name)
