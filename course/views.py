from django.shortcuts import render, redirect
from .models import Course, Apply
from .forms import AddCourse, ApplyForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .filter import CourseFilter


# Create your views here.


def home(request):
    return render(request, 'course/index.html')


def course_list(request):
    courses = Course.objects.all()
    filter = CourseFilter(request.GET, queryset=courses)
    courses = filter.qs
    paginator = Paginator(courses, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'courses': page_obj, 'filter': filter}
    return render(request, 'course/course_list.html', context)


def course_details(request, id):
    course = Course.objects.get(id=id)
    app = Apply.objects.filter(course=course).count()
    if request.method == 'POST':
        form = ApplyForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.course = course
            myform.save()
    else:
        form = ApplyForm()

    context = {'course': course, 'form': form, 'app': app}
    return render(request, 'course/course_details.html', context)


@login_required
def add_course(request):
    if request.method == 'POST':
        form = AddCourse(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('course:course_list'))
    else:
        form = AddCourse()
    return render(request, 'course/add_course.html', {'form': form})
