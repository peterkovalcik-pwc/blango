from django.http import HttpResponse

def index(request):
    return HttpResponse("This is blog module.")
