# Generated by Django 3.1.6 on 2021-08-14 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_auto_20210814_0523'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postfiles',
            old_name='files',
            new_name='file',
        ),
    ]
