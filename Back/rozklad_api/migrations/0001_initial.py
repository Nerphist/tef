# Generated by Django 2.1.5 on 2019-03-06 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('lesson_name', models.CharField(max_length=255)),
                ('teacher', models.CharField(max_length=255, null=True)),
                ('day_number', models.IntegerField()),
                ('lesson_number', models.IntegerField()),
                ('lesson_week', models.IntegerField()),
                ('lesson_room', models.CharField(max_length=255, null=True)),
                ('lesson_type', models.CharField(max_length=255, null=True)),
                ('group_name', models.CharField(max_length=255)),
            ],
        ),
    ]
