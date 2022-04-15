# Generated by Django 4.0.4 on 2022-04-15 14:45

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_remove_card_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='image',
            field=cloudinary.models.CloudinaryField(default=1, max_length=255, verbose_name='image'),
            preserve_default=False,
        ),
    ]