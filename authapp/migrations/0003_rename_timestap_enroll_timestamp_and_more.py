# Generated by Django 4.1.7 on 2023-03-12 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_enroll_membershipplan_trainer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enroll',
            old_name='timeStap',
            new_name='timeStamp',
        ),
        migrations.RenameField(
            model_name='trainer',
            old_name='timeStap',
            new_name='timeStamp',
        ),
        migrations.AddField(
            model_name='enroll',
            name='DueDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='enroll',
            name='paymentStatus',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
        migrations.AddField(
            model_name='enroll',
            name='price',
            field=models.IntegerField(blank=True, max_length=55, null=True),
        ),
    ]
