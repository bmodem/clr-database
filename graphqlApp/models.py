# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bundle(models.Model):
    TYPE_CHOICES = (('bundle', 'bundle'),
                    ('pundle', 'pundle'))
    bundle_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=6, choices=TYPE_CHOICES, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bundle'
        unique_together = (('name', 'type'),)


class BundlePackage(models.Model):
    TYPE_CHOICES = (('include', 'include'),
                    ('package', 'package'))
    bundle_id = models.ForeignKey('Bundle.bundle_id', on_delete=models.CASCADE)
    package_id = models.ForeignKey('Package.package_id', on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, blank=True, null=True)
    from_release = models.IntegerField(blank=True, null=True)
    to_release = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bundle_package'
        abstract = True


class BundleProperty(models.Model):
    bundle_id = models.ForeignKey('Bundle.bundle_id', on_delete=models.CASCADE)
    key = models.CharField(max_length=255)
    value = models.TextField(blank=True, null=True)
    from_release = models.IntegerField(blank=True, null=True)
    to_release = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bundle_property'
        abstract = True


class File(models.Model):
    TYPE_CHOICES = (('file', 'file'),
                    ('link', 'link'),
                    ('directory', 'directory'))
    file_id = models.AutoField(primary_key=True)
    path = models.CharField(max_length=2048)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'file'
        unique_together = (('path', 'type'),)


class Package(models.Model):
    package_id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'package'


class PackageFile(models.Model):
    package_id = models.ForeignKey('Package.package_id', on_delete=models.CASCADE)
    file_id = models.ForeignKey('File.file_id', on_delete=models.CASCADE)
    from_release = models.IntegerField(blank=True, null=True)
    to_release = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'package_file'
        abstract = True


class PackageProperty(models.Model):
    package_id = models.ForeignKey('Package.package_id', on_delete=models.CASCADE)
    key = models.CharField(max_length=255)
    value = models.TextField()
    from_release = models.IntegerField(blank=True, null=True)
    to_release = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'package_property'
        abstract = True
