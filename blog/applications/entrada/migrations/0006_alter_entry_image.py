# Generated by Django 4.2.5 on 2023-09-16 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrada', '0005_alter_entry_puclic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='image',
            field=models.ImageField(default=False, null=True, upload_to='Entry', verbose_name='Imagen'),
        ),
    ]