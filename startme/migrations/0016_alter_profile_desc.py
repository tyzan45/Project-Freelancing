# Generated by Django 4.1.4 on 2023-01-29 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startme', '0015_alter_profile_instagram'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='desc',
            field=models.CharField(default='desc_text', max_length=200, null=True),
        ),
    ]
