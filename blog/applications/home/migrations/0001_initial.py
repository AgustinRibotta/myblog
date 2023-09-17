# Generated by Django 4.2.5 on 2023-09-16 19:59

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('full_name', models.CharField(max_length=60, verbose_name='Nombres')),
                ('email', models.CharField()),
                ('messagge', models.TextField()),
            ],
            options={
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'Mensajes',
            },
        ),
        migrations.CreateModel(
            name='Hoome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=50, verbose_name='Nombre')),
                ('description', models.TextField()),
                ('about_title', models.CharField(max_length=50, verbose_name='Titulo Nosotros')),
                ('contac_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email de Contacto')),
                ('phone', models.CharField(max_length=20, verbose_name='Telefono Contacto')),
            ],
            options={
                'verbose_name': 'Pagina Principal',
                'verbose_name_plural': 'Pagina Principal',
            },
        ),
        migrations.CreateModel(
            name='Suscribers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('email', models.CharField()),
            ],
            options={
                'verbose_name': 'Suscripto',
                'verbose_name_plural': 'Suscriptores',
            },
        ),
    ]
