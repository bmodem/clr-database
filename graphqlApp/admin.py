from django.contrib import admin
from .models import Bundle, Package, BundlePackage, PackageFile, BundleProperty, File, PackageProperty


# Register your models here.
@admin.register(Bundle)
class BundleAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    pass


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    pass

