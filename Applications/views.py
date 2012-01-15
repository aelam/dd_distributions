# Create your views here.
import os
import settings
import django.core.handlers.wsgi

from django.http import HttpResponse,Http404
import os
import datetime

def index(request):
    return HttpResponse("Hello, World.")


def test_application(request):
    return HttpResponse("Hello")

def now(request):
    now = datetime.datetime.now()
    html = "<html><body><b>It is now %s.</b></body></html>" % now
    print html
    return HttpResponse(now)

def arg_test(request,offset):
    """

    """
    try:
        offset = int(offset)
    except ValueError:
        print("ValueError")
        raise Http404()

    result = "offset : %s " % (offset)
    return HttpResponse(result)

def test_static_files(request):
#    html = "<a href=\"/Users/ryan/Sites/hi.jpg\">"
    html = "<a href=\"http://127.0.0:8000/static/hi.jpg\">"
    html = "<img src=\"http://127.0.0.1:8000/static/images/hi.jpg\">"
    #    html = "testuuuur"
    print html
    return HttpResponse(html)


