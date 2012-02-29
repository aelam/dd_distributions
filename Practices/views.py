# Create your views here.
from django.http import HttpResponse,Http404


def practices(request):
    return HttpResponse("Practices")

