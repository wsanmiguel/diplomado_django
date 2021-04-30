# Generated by Django 3.2 on 2021-04-26 13:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('serial', models.CharField(blank=True, max_length=150, null=True)),
                ('inventory', models.CharField(blank=True, max_length=150, null=True)),
                ('image', models.CharField(blank=True, max_length=300, null=True)),
                ('status', models.CharField(choices=[('A', 'Activo'), ('N', 'Anulado'), ('R', 'Reparación'), ('P', 'Prestado'), ('B', 'Baja')], default='A', max_length=1)),
            ],
            options={
                'verbose_name': 'Activo',
                'verbose_name_plural': 'Activos',
            },
        ),
        migrations.CreateModel(
            name='AssetField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Campo de Activo',
                'verbose_name_plural': 'Campos de Activos',
            },
        ),
        migrations.CreateModel(
            name='AssetType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('inventory', models.BooleanField(default=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Tipo de Activos',
                'verbose_name_plural': 'Tipos de Activos',
            },
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Edificio',
                'verbose_name_plural': 'Edificios',
            },
        ),
        migrations.CreateModel(
            name='CostCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('code', models.CharField(max_length=200, verbose_name='Código')),
                ('active', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Centro de Costos',
                'verbose_name_plural': 'Centros de Costos',
            },
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.CharField(max_length=2, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Nombre')),
                ('active', models.BooleanField(default=True, verbose_name='Activo')),
            ],
            options={
                'verbose_name': 'Tipo de Documento',
                'verbose_name_plural': 'Tipos de Documento',
            },
        ),
        migrations.CreateModel(
            name='Drop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Baja',
                'verbose_name_plural': 'Bajas',
            },
        ),
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Planta de Edificio',
                'verbose_name_plural': 'Plantas de Edificio',
            },
        ),
        migrations.CreateModel(
            name='Maker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('active', models.BooleanField(default=True, verbose_name='Activo')),
            ],
            options={
                'verbose_name': 'Fabricante',
                'verbose_name_plural': 'Fabricantes',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Paciente',
                'verbose_name_plural': 'Pacientes',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('code', models.CharField(blank=True, max_length=50, null=True, verbose_name='Código')),
                ('active', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
            },
        ),
        migrations.CreateModel(
            name='Sectional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('address', models.CharField(blank=True, max_length=250, null=True, verbose_name='Dirección')),
                ('pattern_inventory', models.CharField(blank=True, max_length=30, null=True, verbose_name='Patrón de Inventario')),
                ('active', models.BooleanField(default=True, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Seccional',
                'verbose_name_plural': 'Seccionales',
            },
        ),
        migrations.CreateModel(
            name='Space',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Espacio de Piso',
                'verbose_name_plural': 'Espacios de Piso',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
            },
        ),
        migrations.CreateModel(
            name='Third',
            fields=[
                ('identification', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Identificación')),
                ('first_name', models.CharField(max_length=100, verbose_name='Nombres')),
                ('last_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Apellidos')),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Teléfono')),
                ('address', models.CharField(blank=True, max_length=200, null=True, verbose_name='Dirección')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento')),
                ('document_type', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='fixed_assets.documenttype')),
            ],
            options={
                'verbose_name': 'Tercero',
                'verbose_name_plural': 'Terceros',
            },
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Traslado',
                'verbose_name_plural': 'Traslados',
            },
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='fixed_assets.building')),
                ('flat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='fixed_assets.flat')),
                ('space', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='fixed_assets.space')),
            ],
            options={
                'verbose_name': 'Bodega',
                'verbose_name_plural': 'Bodegas',
            },
        ),
        migrations.CreateModel(
            name='TransferField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='fixed_assets.assetfield')),
                ('transfer', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='fixed_assets.transfer')),
            ],
            options={
                'verbose_name': 'Campo de Traslado',
                'verbose_name_plural': 'Campos de Traslados',
            },
        ),
        migrations.CreateModel(
            name='TransferDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('value', models.TextField(blank=True, null=True)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='fixed_assets.asset')),
                ('asset_field', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='fixed_assets.assetfield')),
                ('transfer', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='fixed_assets.transfer')),
            ],
            options={
                'verbose_name': 'Detalle de Traslado',
                'verbose_name_plural': 'Detalle de Traslados',
            },
        ),
        migrations.CreateModel(
            name='DropDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('asset', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='fixed_assets.asset')),
                ('drop', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='fixed_assets.drop')),
            ],
            options={
                'verbose_name': 'Detalle de Baja',
                'verbose_name_plural': 'Detalle de Bajas',
            },
        ),
        migrations.AddField(
            model_name='building',
            name='sectional',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='fixed_assets.sectional'),
        ),
        migrations.AddField(
            model_name='asset',
            name='asset_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='fixed_assets.assettype'),
        ),
        migrations.AddField(
            model_name='asset',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='fixed_assets.supplier'),
        ),
        migrations.CreateModel(
            name='Collaborator',
            fields=[
                ('third_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fixed_assets.third')),
                ('cost_center', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='fixed_assets.costcenter')),
                ('position', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='fixed_assets.position')),
                ('sectional', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='fixed_assets.sectional')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Colaborador',
                'verbose_name_plural': 'Colaboradores',
            },
            bases=('fixed_assets.third',),
        ),
    ]
