# Generated by Django 5.1.2 on 2024-11-30 18:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudyProgram',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('student_id', models.CharField(max_length=255)),
                ('mobile', models.CharField(max_length=15)),
                ('studyprogram', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentList.studyprogram')),
            ],
        ),
    ]
