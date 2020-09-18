# Generated by Django 3.1.1 on 2020-09-15 03:33

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_about_background_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='primary_color',
            field=colorfield.fields.ColorField(default='#138d69', max_length=18),
        ),
        migrations.AddField(
            model_name='about',
            name='secondary_color',
            field=colorfield.fields.ColorField(default='#d6d9dc', max_length=18),
        ),
        migrations.AddField(
            model_name='about',
            name='text_color',
            field=colorfield.fields.ColorField(default='#96999b', max_length=18),
        ),
    ]
