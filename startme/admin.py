from django.contrib import admin
from .models import *
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('name',)

admin.site.register(Profile, ProfileAdmin)
