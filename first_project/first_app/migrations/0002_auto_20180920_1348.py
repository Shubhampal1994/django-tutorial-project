# Generated by Django 2.1.1 on 2018-09-20 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accessrecord',
            old_name='data',
            new_name='date',
        ),
    ]
