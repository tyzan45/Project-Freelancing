from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(default='Enter Your Name', max_length=200, null=True)
    title = models.CharField(default='Title of the project', max_length=200, null=True)

    FREELANCING_TOPICS = [
        ('web_dev', 'Full Stack Web Development'),
        ('graphic_design', 'Graphic Design'),
        ('content_writing', 'Content Writing'),
        ('seo_specialist', 'SEO Specialist'),
        ('data_analysis', 'Data Analysis'),
        ('mobile_dev', 'Mobile App Development'),
        ('digital_marketing', 'Digital Marketing'),
        ('cloud_computing', 'Cloud Computing'),
        ('cyber_security', 'Cyber Security'),
        ('ui_ux_design', 'UI/UX Design'),
    ]

    
    desc = models.CharField(
        max_length=50,
        choices=FREELANCING_TOPICS,
        default='web_dev',  # Set a default option
        null=True
    )

    profile_img = models.ImageField(default='media/default.jpg', upload_to='media', null=True, blank=True)
    images = models.ImageField(default='media/default.jpg', upload_to='media', null=False)
    instagram = models.URLField(default='https://www.instagram.com', max_length=200, null=True)
    projectcomplete = models.CharField(default='None', max_length=3, null=True)
    experience = models.CharField(default='None', max_length=1, null=True)
    totalclients = models.CharField(default='None', max_length=2, null=True)
    reviews = models.CharField(default='None', max_length=3, null=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
