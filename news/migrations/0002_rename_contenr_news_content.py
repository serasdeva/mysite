# Generated by Django 4.0.4 on 2022-05-17 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='contenr',
            new_name='content',
        ),
    ]
