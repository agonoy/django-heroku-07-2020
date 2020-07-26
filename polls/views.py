from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. 90e13578 is the polls index.")
