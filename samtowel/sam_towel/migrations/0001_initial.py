# Generated by Django 2.0.1 on 2020-07-02 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RiderModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=20)),
                ('lastName', models.CharField(max_length=20)),
                ('nickName', models.CharField(max_length=30)),
                ('sport', models.CharField(max_length=15)),
            ],
        ),
    ]
