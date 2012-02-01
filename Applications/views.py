# Create your views here.
import os
import settings
import django.core.handlers.wsgi
from Applications.models import Applicaton
from django.template import Context,loader

from django.http import HttpResponse,Http404
import os
import datetime

def index(request):
    return HttpResponse("Hello, World.")

def apps(request):
    app_list = Applicaton.objects.all()
    print app_list
#    loader.get_template()
    output = ', '.join([p.name for p in app_list])
    return HttpResponse("return an app list: %s " % output)

def detail(request,app_id):
    return HttpResponse("this is app's detail : %s " % app_id)


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


