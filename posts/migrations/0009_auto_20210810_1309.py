# Generated by Django 3.1.6 on 2021-08-10 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20210810_1000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='files',
            new_name='file',
        ),
    ]
