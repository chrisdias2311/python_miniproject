# Generated by Django 4.1.7 on 2023-03-12 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enroll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fullname', models.CharField(max_length=25)),
                ('Email', models.EmailField(max_length=254)),
                ('Gender', models.CharField(max_length=12)),
                ('PhoneNumber', models.CharField(max_length=12)),
                ('DOB', models.CharField(max_length=50)),
                ('SelectMembershipplan', models.CharField(max_length=200)),
                ('SelectTrainer', models.CharField(max_length=55)),
                ('Referenec', models.CharField(max_length=55)),
                ('Address', models.TextField()),
                ('timeStap', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MembershipPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.CharField(max_length=185)),
                ('price', models.IntegerField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('gender', models.CharField(max_length=12)),
                ('phone', models.CharField(max_length=12)),
                ('salary', models.IntegerField(max_length=25)),
                ('timeStap', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
