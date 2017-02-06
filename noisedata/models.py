from django.db import models

class Dummy(models.Model):
    name = models.CharField(max_length=150)
    position = models.FloatField()

    def __unicode__(self):
        return unicode(self.name)
