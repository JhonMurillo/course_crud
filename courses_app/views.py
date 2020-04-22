# Create your views here.
from django.http import JsonResponse
from .models import Course


def get_courses(request):
    courses = list(Course.objects.values())
    return JsonResponse(courses, safe=False) 
