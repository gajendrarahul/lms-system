# Generated by Django 2.2.4 on 2019-10-20 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_announcement'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='manager',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='manager.Manager'),
        ),
    ]