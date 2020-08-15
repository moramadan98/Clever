from django import forms
from .models import Apply, Course


class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = '__all__'
        exclude = ['course']


class AddCourse(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'
