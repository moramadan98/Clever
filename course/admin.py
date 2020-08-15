from django.contrib import admin
from .models import Course, Category, Apply

# Register your models here.

admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Apply)
