# Generated by Django 3.1.1 on 2020-09-14 16:03

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_about_site_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='background_color',
            field=colorfield.fields.ColorField(default='#868E96', max_length=18),
        ),
    ]