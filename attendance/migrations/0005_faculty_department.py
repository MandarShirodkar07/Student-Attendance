# Generated by Django 5.0.2 on 2025-03-27 07:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0004_remove_faculty_department_alter_degree_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='faculty',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='attendance.department'),
        ),
    ]
