# Generated by Django 4.2.5 on 2023-09-16 20:43

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entrada', '0007_alter_entry_image_alter_entry_puclic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=True, null=True, verbose_name='Contenido'),
        ),
    ]
