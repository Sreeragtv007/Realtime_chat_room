# Generated by Django 4.2 on 2024-06-07 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_alter_room_room_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
