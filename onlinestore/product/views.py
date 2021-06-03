from django.http import JsonResponse
from django.shortcuts import render

from .models import Student


def student_detail(request, registrationNo):
    try:
        student = Student.objects.get(registrationNo=registrationNo)
        data = {"student": {
            "name": student.name,
            "registrationNo": student.registrationNo,
            "cgpa": student.cgpa}}

    except Student.DoesNotExist:
        data = "not found"

    return render(request, "student.html", {'data': data})
    # return response


def student_list(request):
    students = Student.objects.all()
    data = {"students": list(students.values())}
    response = JsonResponse(data)
    return render(request, "students.html", {'data': data})
