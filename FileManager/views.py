from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.conf import settings
from django.contrib.csrf.middleware import csrf_exempt

import os


def upload_file(request):
    print "-----------------------------\nrequest.Files"
    if request.method == 'POST':
        file = request.FILES.get('filename','')
        filename=file.name
        print settings.MEDIA_ROOT
        print filename
        print file
        fname = os.path.join(settings.MEDIA_ROOT,filename)
        print "fname"
        print fname
        if os.path.exists(fname):
            os.remove(fname)
            dirs= os.path.dirname(fname)
            if not os.path.exists(dirs):
                os.makedirs(dirs)

        print os.path.isfile(fname)
        if True: #.path.isfile(fname):
            os.remove(fname)
            fp = open(fname, 'wb')
#            fp.write(file)
            print file.chunks()
            print file.size
            for content in file.chunks():
                print content
                fp.write(content)
            fp.close()

            return HttpResponse('ok')
    return render_to_response("upload.html",locals())

upload_file = csrf_exempt(upload_file)