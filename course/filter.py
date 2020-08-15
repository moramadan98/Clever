import django_filters
from .models import Course


class CourseFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    instructor = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Course
        fields = '__all__'
        exclude = ['image']
