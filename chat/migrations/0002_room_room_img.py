# Generated by Django 4.2 on 2024-06-07 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='room_img',
            field=models.ImageField(blank=True, null=True, upload_to='room_images'),
        ),
    ]
