# Generated by Django 2.2 on 2019-04-24 12:45

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_Name', models.CharField(max_length=120)),
                ('pillar_Type', models.CharField(choices=[('ASD', 'ASD'), ('ISTD', 'ISTD'), ('EPD', 'EPD'), ('ESD', 'ESD'), ('FRESHMORE', 'FRESHMORE'), ('MASTERS', 'MASTERS'), ('PHD', 'PHD'), ('NONE', 'NONE')], max_length=10)),
                ('event_Name', models.CharField(default='None', max_length=120)),
                ('lecturer', models.CharField(max_length=50)),
                ('class_Enrolled', models.CharField(default='', max_length=6)),
                ('description', models.TextField(blank=True, null=True)),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('start_Time', models.TimeField(choices=[(datetime.time(7, 0), '07:00'), (datetime.time(8, 0), '08:00'), (datetime.time(9, 0), '09:00'), (datetime.time(10, 0), '10:00'), (datetime.time(11, 0), '11:00'), (datetime.time(12, 0), '12:00'), (datetime.time(13, 0), '13:00'), (datetime.time(14, 0), '14:00'), (datetime.time(15, 0), '15:00'), (datetime.time(16, 0), '16:00'), (datetime.time(17, 0), '17:00'), (datetime.time(18, 0), '18:00'), (datetime.time(19, 0), '19:00'), (datetime.time(20, 0), '20:00'), (datetime.time(21, 0), '21:00'), (datetime.time(22, 0), '22:00'), (datetime.time(23, 0), '23:00'), (datetime.time(7, 30), '07:30'), (datetime.time(8, 30), '08:30'), (datetime.time(9, 30), '09:30'), (datetime.time(10, 30), '10:30'), (datetime.time(11, 30), '11:30'), (datetime.time(12, 30), '12:30'), (datetime.time(13, 30), '13:30'), (datetime.time(14, 30), '14:30'), (datetime.time(15, 30), '15:30'), (datetime.time(16, 30), '16:30'), (datetime.time(17, 30), '17:30'), (datetime.time(18, 30), '18:30'), (datetime.time(19, 30), '19:30'), (datetime.time(20, 30), '20:30'), (datetime.time(21, 30), '21:30'), (datetime.time(22, 30), '22:30'), (datetime.time(23, 30), '23:30')])),
                ('event_Duration', models.IntegerField(choices=[(15, '15'), (30, '30'), (45, '45'), (60, '60'), (75, '75'), (90, '90'), (105, '105'), (120, '120'), (135, '135'), (150, '150'), (165, '165'), (180, '180')], default=0)),
                ('location', models.IntegerField(choices=[(1, 'any'), (2, 'Lecture Theatre')])),
                ('is_Event', models.BooleanField(default=False)),
                ('initiated_By', models.CharField(default='Nobody', max_length=50)),
                ('is_Conflicting', models.BooleanField(default=False)),
                ('day_Of_Week', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(7), django.core.validators.MinValueValidator(1)])),
            ],
        ),
    ]
