# Generated by Django 4.1.4 on 2023-07-01 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katzegram', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
    ]
