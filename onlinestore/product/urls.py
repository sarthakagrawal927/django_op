from django.urls import path
from .views import student_detail, student_list, about

urlpatterns = [
    path("students/", student_list, name='student-list'),
    path("students/<int:registrationNo>/",
         student_detail, name='student-detail'),
    path("about",
         about, name='about'),
]
