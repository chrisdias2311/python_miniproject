# Generated by Django 4.1.7 on 2023-04-12 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0006_attendance'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='phonenumber',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
