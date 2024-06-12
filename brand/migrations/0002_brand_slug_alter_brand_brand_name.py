# Generated by Django 5.0.6 on 2024-06-10 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='brand',
            name='brand_name',
            field=models.CharField(max_length=100),
        ),
    ]