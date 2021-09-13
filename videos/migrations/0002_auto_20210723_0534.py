# Generated by Django 3.1.6 on 2021-07-23 05:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='bad',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='video',
            name='good',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='video',
            name='url',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='video',
            name='views',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='video',
            name='licence',
            field=models.CharField(choices=[('U', 'Universal'), ('S', 'Universal/Adult'), ('A', 'Adult'), ('X', 'XXX-Content')], max_length=1),
        ),
    ]
