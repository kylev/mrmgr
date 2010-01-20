from django.db import models

class Rack(models.Model):
    name = models.CharField(primary_key=True, max_length=128)

    def __unicode__(self):
        return self.name


class Machine(models.Model):
    name = models.CharField(primary_key=True, max_length=255, unique=True)
    rack = models.ForeignKey(Rack)
    position = models.IntegerField(default=1)
    u_space = models.IntegerField(default=1)

    def __unicode__(self):
        return "%s (%dU)" % (self.name, self.u_space)
