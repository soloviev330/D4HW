# Generated by Django 3.1.4 on 2020-12-21 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0004_auto_20201221_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='p_library.publisher', verbose_name='Издательство'),
            preserve_default=False,
        ),
    ]
