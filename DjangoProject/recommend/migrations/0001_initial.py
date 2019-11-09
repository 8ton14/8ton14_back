# Generated by Django 2.2.7 on 2019-11-09 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=100)),
                ('male', models.FloatField(default=0.0)),
                ('female', models.FloatField(default=0.0)),
                ('age10', models.FloatField(default=0.0)),
                ('age20', models.FloatField(default=0.0)),
                ('age30', models.FloatField(default=0.0)),
                ('age40', models.FloatField(default=0.0)),
                ('age50older', models.FloatField(default=0.0)),
                ('student', models.FloatField(default=0.0)),
                ('exercise', models.FloatField(default=0.0)),
                ('healthcare', models.FloatField(default=0.0)),
                ('beauty', models.FloatField(default=0.0)),
                ('game', models.FloatField(default=0.0)),
                ('it', models.FloatField(default=0.0)),
                ('fashion', models.FloatField(default=0.0)),
            ],
        ),
    ]