# Generated by Django 5.0.3 on 2024-03-16 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='name',
            field=models.CharField(blank=True, max_length=70, null=True, unique=True, verbose_name='название'),
        ),
    ]
