from django.db import models

# Create your models here.


class Monday(models.Model):
    classname = models.CharField(max_length=32)
    classstart = models.IntegerField()
    classend = models.IntegerField()


class Tuesday(models.Model):
    classname = models.CharField(max_length=32)
    classstart = models.IntegerField()
    classend = models.IntegerField()


class Wednesday(models.Model):
    classname = models.CharField(max_length=32)
    classstart = models.IntegerField()
    classend = models.IntegerField()


class Thursday(models.Model):
    classname = models.CharField(max_length=32)
    classstart = models.IntegerField()
    classend = models.IntegerField()


class Friday(models.Model):
    classname = models.CharField(max_length=32)
    classstart = models.IntegerField()
    classend = models.IntegerField()


class dismonday(models.Model):
    theclass = models.CharField(max_length=32)


class distuesday(models.Model):
    theclass = models.CharField(max_length=32)


class diswednesday(models.Model):
    theclass = models.CharField(max_length=32)


class disthursday(models.Model):
    theclass = models.CharField(max_length=32)


class disfriday(models.Model):
    theclass = models.CharField(max_length=32)


class thematters(models.Model):
    thematter = models.CharField(max_length=32)


class theattendants(models.Model):
    theattendant = models.CharField(max_length=32)
    master = models.IntegerField()


class scelectedbg(models.Model):
    bgname = models.CharField(max_length=64)
