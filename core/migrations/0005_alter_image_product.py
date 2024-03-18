# Generated by Django 5.0.3 on 2024-03-18 04:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_product_images_image_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='image', to='core.product'),
        ),
    ]
