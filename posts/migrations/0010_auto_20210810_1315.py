# Generated by Django 3.1.6 on 2021-08-10 13:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20210810_1309'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='file',
            new_name='files',
        ),
    ]
