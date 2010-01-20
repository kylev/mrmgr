from django.db import models

class Rack(models.Model):
    name = models.CharField(primary_key=True, max_length=128)

    def __unicode__(self):
        return self.name


class Platform(models.Model):
    RAID_CHOICES = ((u'none', u'none'),
                    (u'generic', u'generic'),
                    (u'RAID1', u'RAID1'),
                    (u'RAID5', u'RAID5'),
                    (u'RAID10', u'RAID10'),
                    )

    name = models.CharField(max_length=255, unique=True)
    u_space = models.PositiveIntegerField(default=1)
    cpu_mhz = models.PositiveIntegerField()
    fsb_mhz = models.PositiveIntegerField()
    # TODO Below here might be Machine specific...
    ram_mb = models.PositiveIntegerField()
    raid = models.CharField(max_length=8, choices=RAID_CHOICES)

    def __unicode__(self):
        return self.name


class Machine(models.Model):
    name = models.CharField(primary_key=True, max_length=255, unique=True)
    rack = models.ForeignKey(Rack)
    position = models.IntegerField(default=1)
    platform = models.ForeignKey(Platform)

    def __unicode__(self):
        return self.name
