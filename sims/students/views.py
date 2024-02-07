from django.shortcuts import HttpResponse, render

# views for student registration and managemnt webpage

def index(request):
    """returns a simple test view of index"""
    # return HttpResponse("This is mmy first index page in django")
    return render(request, "index.html")
