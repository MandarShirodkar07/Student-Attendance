# Generated by Django 5.0.2 on 2025-03-27 07:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_alter_degree_name_alter_department_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faculty',
            name='department',
        ),
        migrations.AlterField(
            model_name='degree',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='attendance.department'),
        ),
    ]
