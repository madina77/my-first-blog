# Generated by Django 2.0 on 2017-12-23 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20171223_1306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='height_field',
        ),
        migrations.RemoveField(
            model_name='post',
            name='width_field',
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
