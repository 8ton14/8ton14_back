# Generated by Django 2.2.7 on 2019-11-09 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0002_auto_20191109_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='common_price',
            field=models.IntegerField(default=0),
        ),
    ]
