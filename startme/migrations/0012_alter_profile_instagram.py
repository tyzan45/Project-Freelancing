# Generated by Django 4.1.4 on 2023-01-26 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startme', '0011_alter_profile_projectcomplete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='instagram',
            field=models.URLField(default='https://www.instagram.com', null=True),
        ),
    ]
