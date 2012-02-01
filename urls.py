from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
#import dd_distributions.Application
#from Application.views import test_application
from Applications.views import test_application
#from FileManager.views import upload_file

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dd_distributions.views.home', name='home'),
    # url(r'^dd_distributions/', include('dd_distributions.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/', 'dd_distributions.Applications.views.test_application'),
    url(r'^now/', 'dd_distributions.Applications.views.now'),
    url(r'^arg/(\d{1,2})/', 'dd_distributions.Applications.views.arg_test'),
    url(r'^teststatic/', 'dd_distributions.Applications.views.test_static_files'),
    url(r'^upload/','dd_distributions.FileManager.views.upload_file'),

    url(r'^apps/','dd_distributions.Applications.views.apps'),

)

