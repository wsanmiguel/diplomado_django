from django.contrib import admin

# Register your models here.
from .models import DocumentType, Supplier, Position, CostCenter
from .models import Sectional, Building, Flat, Space, Warehouse
from .models import Maker, AssetType, Asset, AssetField, Transfer
from .models import TransferField, TransferDetail, Drop, DropDetail
from .models import Collaborator


@admin.register(DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('active',)


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    pass


@admin.register(CostCenter)
class CostCenterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code')


@admin.register(Sectional)
class SectionalAdmin(admin.ModelAdmin):
    pass


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    pass


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    pass


@admin.register(Space)
class SpaceAdmin(admin.ModelAdmin):
    pass


@admin.register(Warehouse)
class WareHouseAdmin(admin.ModelAdmin):
    pass


@admin.register(Maker)
class MakerAdmin(admin.ModelAdmin):
    pass


@admin.register(AssetType)
class AssetTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'inventory', 'active')


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    pass


@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    pass


@admin.register(TransferField)
class TransferFieldAdmin(admin.ModelAdmin):
    pass


@admin.register(TransferDetail)
class TransferDetailAdmin(admin.ModelAdmin):
    pass


@admin.register(Drop)
class DropAdmin(admin.ModelAdmin):
    pass


@admin.register(DropDetail)
class DropDetailAdmin(admin.ModelAdmin):
    pass


@admin.register(Collaborator)
class CollaboratorAdmin(admin.ModelAdmin):
    pass
