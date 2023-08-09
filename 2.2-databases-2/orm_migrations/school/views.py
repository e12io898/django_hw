from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    ordering = 'group'
    objects = Student.objects.all().order_by(ordering)
    context = {'object_list': objects}

    return render(request, template, context)
