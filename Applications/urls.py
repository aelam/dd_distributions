from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('Applications.views',
    url(r'^$','apps'),
    url(r'^(?P<app_id>\d+)/$','detail'),
    url(r'^test$','test_application'),
    url(r'^upload$','upload'),

)