# Generated by Django 4.2 on 2024-06-09 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_alter_room_room_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='disc',
            field=models.TextField(blank=True, null=True),
        ),
    ]
