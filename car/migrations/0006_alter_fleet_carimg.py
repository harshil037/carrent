# Generated by Django 3.2.4 on 2021-07-01 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0005_alter_fleet_carimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fleet',
            name='carImg',
            field=models.ImageField(upload_to='fleet/'),
        ),
    ]
