# Generated by Django 3.1.6 on 2021-07-11 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_delete_follow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(default='images/default.jpg', upload_to='profile_pics'),
        ),
    ]
