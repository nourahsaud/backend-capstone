# Generated by Django 4.0.6 on 2022-07-27 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_companyprofile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='avatar',
            field=models.URLField(),
        ),
    ]
