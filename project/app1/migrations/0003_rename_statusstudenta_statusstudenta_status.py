# Generated by Django 4.2.1 on 2023-06-11 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_statusstudenta_alter_status_status_alter_uloge_role'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statusstudenta',
            old_name='statusStudenta',
            new_name='status',
        ),
    ]
