# Generated by Django 5.0.6 on 2024-06-10 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0002_brand_slug_alter_brand_brand_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
