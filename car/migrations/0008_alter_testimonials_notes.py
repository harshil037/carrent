# Generated by Django 3.2.4 on 2021-07-08 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0007_alter_testimonials_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonials',
            name='notes',
            field=models.TextField(editable=False),
        ),
    ]
