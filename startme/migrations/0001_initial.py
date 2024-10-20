# Generated by Django 4.1.4 on 2023-01-20 15:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='John Murphy (Default)', max_length=200, null=True)),
                ('title', models.CharField(default='This is the defualt', max_length=200, null=True)),
                ('desc', models.CharField(default='Hey, this is the default descp.', max_length=200, null=True)),
                ('profile_img', models.ImageField(blank=True, default='images/default.jpg', null=True, upload_to='images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
