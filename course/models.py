from django.db import models

# Create your models here.


certification = (
    ('yes', 'yes'),
    ('no', 'no')
)


class Course(models.Model):
    title = models.CharField(max_length=150)
    instructor = models.CharField(max_length=150)
    duration = models.IntegerField(default=1)
    leactures = models.IntegerField(default=1)
    quizzes = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    description = models.TextField(max_length=200)
    certification = models.CharField(max_length=5, choices=certification)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='course/')

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Apply(models.Model):
    course = models.ForeignKey(Course,  on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name
