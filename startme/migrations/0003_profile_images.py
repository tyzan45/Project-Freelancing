# Generated by Django 4.1.4 on 2023-01-23 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startme', '0002_alter_profile_desc_alter_profile_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='images',
            field=models.ImageField(default='media/default.jpg', upload_to='media/userposts'),
        ),
    ]
