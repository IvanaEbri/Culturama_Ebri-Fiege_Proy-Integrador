# Generated by Django 5.1.1 on 2024-09-30 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_tour', '0004_site_tour_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='site_tour',
            name='tags',
        ),
    ]
