from django.http import JsonResponse

from .models import Student


def student_detail(request, registrationNo):
    try:
        student = Student.objects.get(registrationNo=registrationNo)
        data = {"student": {
            "name": student.name,
            "registrationNo": student.registrationNo,
            "cgpa": student.cgpa}}
        response = JsonResponse(data)

    except Student.DoesNotExist:
        response = JsonResponse({"error": {
            "code": 404, "message": "not found"
        }}, status=404)
    return response


def student_list(request):
    students = Student.objects.all()
    data = {"students": list(students.values())}
    response = JsonResponse(data)
    return response
