# Generated by Django 4.2.1 on 2023-06-11 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_rename_statusstudenta_statusstudenta_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='korisnik',
            name='status',
            field=models.ForeignKey(blank='true', null='true', on_delete=django.db.models.deletion.CASCADE, to='app1.statusstudenta'),
        ),
    ]