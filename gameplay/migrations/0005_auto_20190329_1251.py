# Generated by Django 2.1.7 on 2019-03-29 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay', '0004_auto_20190329_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statusclass',
            name='statuscode',
            field=models.CharField(max_length=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='statusclass',
            name='statusmeaning',
            field=models.CharField(default='First Player To Move', max_length=300),
        ),
    ]