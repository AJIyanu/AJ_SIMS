from django.shortcuts import HttpResponse

# views for student registration and managemnt webpage

def index(request):
    """returns a simple test view of index"""
    return HttpResponse("This is mmy first index page in django")
