# Generated by Django 4.1.6 on 2023-02-08 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camiones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='camiones',
            name='imagen',
            field=models.ImageField(null=True, upload_to='media/camiones', verbose_name='Foto camion'),
        ),
    ]
