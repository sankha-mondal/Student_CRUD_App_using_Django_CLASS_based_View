from django.http import HttpResponse
from django.shortcuts import render
from django.views import View, generic

from Student_App.models import Student

# Create your views here.
class HomeView(View):
    msg = ""
    def get(self, request):
        return HttpResponse(f"<h1>{self.msg}</h1>")




## Get all students and display them in a list view
## http://127.0.0.1:8000/students/
class StudentList_View(generic.ListView):
    model = Student
    # default template name would be 'student_list.html' in the 'Student_App/templates/Student_App/' directory
    # default context object name would be 'student_list' in the template
    template_name = 'Student_App/students_list.html'
    context_object_name = 'students'




## Get a single student and display the details in a detail view
## http://127.0.0.1:8000/student/<id>/
class StudentDetail_View(generic.DetailView):
    model = Student
    # default template name would be 'student_detail.html' in the 'Student_App/templates/Student_App/' directory
    # default context object name would be 'student' in the template
    template_name = 'Student_App/student_detail.html'
    context_object_name = 'student'





## Create a new student using the first method (manual form handling) - Type1
## http://127.0.0.1:8000/student/create_type1/
class StudentCreateType1_View(generic.CreateView):
    model = Student
    # default template name would be 'student_form.html' in the 'Student_App/templates/Student_App/' directory
    # default context object name would be 'form' in the template
    template_name = 'Student_App/student_create_type1.html'
    fields = ['firstname', 'lastname', 'age', 'testscore']

## Create a new student using the second method (using ModelForm)  - Type2
## http://127.0.0.1:8000/student/create_type2/
class StudentCreateType2_View(generic.CreateView):
    model = Student
    # default template name would be 'student_form.html' in the 'Student_App/templates/Student_App/' directory
    # default context object name would be 'form' in the template
    template_name = 'Student_App/student_create_type2.html'
    fields = ['firstname', 'lastname', 'age', 'testscore']




## Update an existing student using the first method (manual form handling) - Type1
## http://127.0.0.1:8000/student/update_type1/<id>/
class StudentUpdateType1_View(generic.UpdateView):
    model = Student
    # default template name would be 'student_form.html' in the 'Student_App/templates/Student_App/' directory
    # default context object name would be 'form' in the template
    template_name = 'Student_App/student_update_type1.html'
    fields = ['age', 'testscore']

## Update an existing student using the second method (using ModelForm) - Type2
## http://127.0.0.1:8000/student/update_type2/<id>/
class StudentUpdateType2_View(generic.UpdateView):
    model = Student
    # default template name would be 'student_form.html' in the 'Student_App/templates/Student_App/' directory
    # default context object name would be 'form' in the template
    template_name = 'Student_App/student_update_type2.html'
    fields = ['age', 'testscore']





## Delete an existing student using the DeleteView
## http://127.0.0.1:8000/student/delete/<id>/
class StudentDeleteView(generic.DeleteView):
    model = Student
    # default template name would be 'student_confirm_delete.html' in the 'Student_App/templates/Student_App/' directory
    # default context object name would be 'student' in the template
    template_name = 'Student_App/student_confirm_delete.html'
    success_url = '/students/'