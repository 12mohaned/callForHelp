# Generated by Django 2.2.5 on 2020-10-12 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Visuals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='median',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
