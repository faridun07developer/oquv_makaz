# Generated by Django 5.0.3 on 2024-10-12 13:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('number_of_srudents', models.IntegerField()),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('percent', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=100)),
                ('subject_time', models.DateTimeField()),
                ('juftmi', models.BooleanField(default=True)),
                ('kurs_price', models.IntegerField()),
                ('subject_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.room')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Pupils',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('fathersname', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=16)),
                ('date_of_birth', models.DateField()),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.subject')),
            ],
        ),
    ]