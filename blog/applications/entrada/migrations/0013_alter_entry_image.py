# Generated by Django 4.2.5 on 2023-09-16 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrada', '0012_alter_entry_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='image',
            field=models.ImageField(blank=True, upload_to='Entry', verbose_name='Imagen'),
        ),
    ]
