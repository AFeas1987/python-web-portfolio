# Generated by Django 3.1.1 on 2020-09-14 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_interests'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='site_title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
