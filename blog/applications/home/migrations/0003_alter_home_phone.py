# Generated by Django 4.2.5 on 2023-09-17 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_hoome_home'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Telefono Contacto'),
        ),
    ]