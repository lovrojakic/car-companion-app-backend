# Generated by Django 5.1.2 on 2024-11-18 15:48

import colorfield.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0009_color_description_color_hex_code_color_is_metallic_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelComponent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'blank': 'Component name cannot be blank.'}, help_text='Name of the default component', max_length=200, verbose_name='name')),
                ('is_required', models.BooleanField(default=True, help_text='Whether this component is required for all vehicles of this model', verbose_name='required')),
            ],
            options={
                'verbose_name': 'Model Component',
                'verbose_name_plural': 'Model Components',
                'db_table': 'model_components',
                'ordering': ['model', 'component_type__name'],
            },
        ),
        migrations.RenameIndex(
            model_name='vehiclemodel',
            new_name='model_name_idx',
            old_name='vehicle_model_name_idx',
        ),
        migrations.RenameIndex(
            model_name='vehiclemodel',
            new_name='model_manufacturer_idx',
            old_name='vehicle_model_manufacturer_idx',
        ),
        migrations.AlterField(
            model_name='color',
            name='hex_code',
            field=colorfield.fields.ColorField(default='#FFFFFF', help_text='Color in hexadecimal format', image_field=None, max_length=25, samples=['#1E40AF', '#047857', '#B91C1C', '#FFFFFF', '#000000', '#6B7280', '#92400E'], verbose_name='color code'),
        ),
        migrations.AddField(
            model_name='modelcomponent',
            name='component_type',
            field=models.ForeignKey(help_text='Type of this component', on_delete=django.db.models.deletion.PROTECT, related_name='model_components', to='vehicle.componenttype', verbose_name='component type'),
        ),
        migrations.AddField(
            model_name='modelcomponent',
            name='model',
            field=models.ForeignKey(help_text='Model this component belongs to', on_delete=django.db.models.deletion.CASCADE, related_name='default_components', to='vehicle.vehiclemodel', verbose_name='vehicle model'),
        ),
        migrations.AlterUniqueTogether(
            name='modelcomponent',
            unique_together={('model', 'name')},
        ),
    ]