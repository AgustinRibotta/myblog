# Generated by Django 4.2.5 on 2023-09-16 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrada', '0013_alter_entry_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='title',
            field=models.CharField(default=1, max_length=50, verbose_name='Titulo'),
            preserve_default=False,
        ),
    ]
