# Generated by Django 2.2.4 on 2019-10-21 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_student_enrolled_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(blank=True, max_length=100, null=True)),
                ('rollno', models.IntegerField()),
                ('assignment', models.FileField(upload_to='')),
            ],
        ),
    ]
