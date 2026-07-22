from django.db import models
from django.urls import reverse

# Create your models here.
class Student(models.Model):
    firstname = models.CharField(max_length=20, null=False)
    lastname = models.CharField(max_length=20, null=False)
    age = models.IntegerField()
    testscore = models.FloatField()

    # Get the absolute URL for the student detail view
    # This method is used to get the URL for the detail view of a student instance.
    # It uses the reverse function to generate the URL based on the 'student-detail' 
    # URL pattern and the primary key (pk) of the student instance.
    def get_absolute_url(self):
        return reverse('student-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return f"{self.firstname} {self.lastname}"