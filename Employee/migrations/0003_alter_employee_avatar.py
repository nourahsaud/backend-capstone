# Generated by Django 4.0.6 on 2022-07-27 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0002_remove_requestemployee_request_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='avatar',
            field=models.ImageField(upload_to=''),
        ),
    ]
