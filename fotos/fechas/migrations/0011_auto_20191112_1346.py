# Generated by Django 2.2.6 on 2019-11-12 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fechas', '0010_auto_20191112_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservainstancia',
            name='reserva',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='fechas.Reserva'),
        ),
    ]
