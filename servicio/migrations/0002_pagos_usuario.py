# Generated by Django 4.1.4 on 2022-12-20 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
        ('servicio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagos',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuario.createuser'),
        ),
    ]