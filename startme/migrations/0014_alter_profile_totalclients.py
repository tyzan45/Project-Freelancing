# Generated by Django 4.1.4 on 2023-01-26 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startme', '0013_alter_profile_instagram'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='totalclients',
            field=models.CharField(default='None', max_length=2, null=True),
        ),
    ]
