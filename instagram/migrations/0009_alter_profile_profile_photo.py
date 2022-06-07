# Generated by Django 4.0.5 on 2022-06-07 22:34

from django.db import migrations, models
import instagram.models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0008_profile_created_profile_first_name_profile_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to=instagram.models.user_directory_path),
        ),
    ]
