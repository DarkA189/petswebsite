# Generated by Django 3.1.7 on 2021-05-03 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='our_price',
            field=models.IntegerField(default=0),
        ),
    ]