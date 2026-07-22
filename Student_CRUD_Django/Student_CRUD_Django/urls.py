"""
URL configuration for Student_CRUD_Django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', HomeView.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Student_App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.HomeView.as_view(msg='Welcome to the Student CRUD Django Application!'), name='home'),

    path('students/', views.StudentList_View.as_view(), name='student-list'),
    path('student/<int:pk>/', views.StudentDetail_View.as_view(), name='student-detail'),

    path('student/create_type1/', views.StudentCreateType1_View.as_view(), name='student-create-type1'),
    path('student/create_type2/', views.StudentCreateType2_View.as_view(), name='student-create-type2'),

    path('student/update_type1/<int:pk>/', views.StudentUpdateType1_View.as_view(), name='student-update-type1'),
    path('student/update_type2/<int:pk>/', views.StudentUpdateType2_View.as_view(), name='student-update-type2'),

    path('student/delete/<int:pk>/', views.StudentDeleteView.as_view(), name='student-delete'),
]
