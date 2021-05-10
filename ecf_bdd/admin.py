from django.contrib import admin
from .models import SchoolYear, User, Project

# Register your models here.
admin.site.register(SchoolYear)
admin.site.register(User)
admin.site.register(Project)