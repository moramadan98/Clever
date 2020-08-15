from django.urls import path, include
from . import views

app_name = 'course'

urlpatterns = [
    path('', views.home, name='home'),
    path('course_list', views.course_list, name='course_list'),
    path('add_course', views.add_course, name='add_course'),
    path('<int:id>', views.course_details, name='course_details'),

]
