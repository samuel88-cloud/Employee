# Generated by Django 2.2.6 on 2020-10-30 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('salary', models.FloatField()),
                ('position', models.CharField(choices=[('1', 'level 1'), ('2', 'level 2'), ('3', 'level 3'), ('4', 'level 4'), ('5', 'level 5'), ('6', 'level 6'), ('7', 'level 7'), ('8', 'level 9'), ('9', 'level 9'), ('10', 'level 10')], max_length=300)),
                ('Address', models.CharField(max_length=500)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
