import graphene
from graphene_django.types import DjangoObjectType
from .models import Bundle, Package, File, BundleProperty, BundlePackage, PackageFile, PackageProperty


class BundlePropertyType(DjangoObjectType):
    class Meta:
        model = BundleProperty
        exclude = ('bundle_id', 'from_release', 'to_release',)


class PackagePropertyType(DjangoObjectType):
    class Meta:
        model = PackageProperty
        exclude = ('package_id', 'from_release', 'to_release',)


class Filetype(DjangoObjectType):
    class Meta:
        model = File
        exclude = ('file_id',)

    bundles = graphene.List(lambda: Bundletype)
    packages = graphene.Field(lambda: PackageType)

    def resolve_bundles(self, info, **kwargs):
        pass

    def resolve_packages(self, info, **kwargs):
        pass


class PackageType(DjangoObjectType):
    class Meta:
        model = Package
        exclude = ('package_id',)

    properties = graphene.Field(PackagePropertyType)
    files = graphene.List(Filetype)
    bundles = graphene.List(lambda: Bundletype)

    def resolve_properties(self, info, **kwargs):
        pass

    def resolve_bundles(self, info, **kwargs):
        pass

    def resolve_files(self, info, **kwargs):
        pass


class Bundletype(DjangoObjectType):
    class Meta:
        model = Bundle
        exclude = ('bundle_id',)

    properties = graphene.List(graphene.NonNull(BundlePropertyType))
    packages = graphene.NonNull(graphene.List(graphene.NonNull(PackageType)))
    files = graphene.NonNull(graphene.List(graphene.NonNull(Filetype)))

    def resolve_properties(BundleProperty, info, **kwargs):
        pass

    def resolve_packages(self, info, **kwargs):
        pass

    def resolve_files(self, info, **kwargs):
        pass


class BundlePackagetype(DjangoObjectType):
    class Meta:
        model = BundlePackage
        exclude = ('bundle_id', 'package_id',)


class PackageFiletype(DjangoObjectType):
    class Meta:
        model = PackageFile
        exclude = ('file_id', 'package_id',)


class Query(graphene.ObjectType):
    bundle = graphene.Field(graphene.NonNull(Bundletype),
                            name=graphene.NonNull(graphene.String),
                            release=graphene.NonNull(graphene.Int)
                            )
    bundles = graphene.List(graphene.NonNull(Bundletype),
                            release=graphene.NonNull(graphene.Int)
                            )
    package = graphene.Field(graphene.NonNull(PackageType),
                             name=graphene.NonNull(graphene.String),
                             release=graphene.NonNull(graphene.Int)
                             )
    packages = graphene.List(graphene.NonNull(PackageType),
                             release=graphene.NonNull(graphene.Int)
                             )
    file = graphene.Field(graphene.NonNull(Filetype),
                          path=graphene.NonNull(graphene.String),
                          release=graphene.NonNull(graphene.Int)
                          )
    files = graphene.List(graphene.NonNull(Filetype),
                          release=graphene.NonNull(graphene.Int)
                          )

    def resolve_bundle(self, info, **kwargs):
        name = kwargs.get('name')
        release = kwargs.get('release')
        if name is not None and release is not None:
            return Bundle.objects.get(name=name)

        return None

    def resolve_bundles(self, info, **kwargs):
        release = kwargs.get('release')
        if release is not None:
            return Bundle.objects.all()

        return None

    def resolve_package(self, info, **kwargs):
        name = kwargs.get('name')
        release = kwargs.get('release')
        if name is not None and release is not None:
            return Package.objects.get(name=name, release=release)

        return None

    def resolve_packages(self, info, **kwargs):
        release = kwargs.get('release')
        if release is not None:
            return Bundle.objects.all()

        return None

    def resolve_file(self, info, **kwargs):
        path = kwargs.get('path')
        release = kwargs.get('release')
        if name is not None and release is not None:
            return File.objects.get(path=path, from_release=release)

        return None

    def resolve_files(self, info, **kwargs):
        release = kwargs.get('release')
        if release is not None:
            return File.objects.all()

        return None
