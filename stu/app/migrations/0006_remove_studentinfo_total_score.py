# Generated by Django 4.1 on 2023-03-23 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_studentinfo_ave_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentinfo',
            name='total_score',
        ),
    ]