# Generated by Django 4.0.6 on 2022-07-27 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='avatar',
            field=models.ImageField(upload_to=''),
        ),
    ]
