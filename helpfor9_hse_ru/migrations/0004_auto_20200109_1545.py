# Generated by Django 2.2.8 on 2020-01-09 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpfor9_hse_ru', '0003_auto_20200109_1542'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='ev_date',
            new_name='event_date',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='ev_name',
            new_name='event_name',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='ev_place',
            new_name='event_place',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='ev_time',
            new_name='event_time',
        ),
        migrations.RenameField(
            model_name='facultative',
            old_name='fac_date',
            new_name='facultative_date',
        ),
        migrations.RenameField(
            model_name='facultative',
            old_name='fac_name',
            new_name='facultative_name',
        ),
        migrations.RenameField(
            model_name='facultative',
            old_name='fac_place',
            new_name='facultative_place',
        ),
        migrations.RenameField(
            model_name='facultative',
            old_name='fac_teacher',
            new_name='facultative_teacher',
        ),
        migrations.RenameField(
            model_name='facultative',
            old_name='fac_time',
            new_name='facultative_time',
        ),
    ]
