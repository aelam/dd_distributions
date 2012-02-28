from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('Practices.views',
    url(r'^$','practices'),
    url(r'^(?P<app_id>\d+)/$','detail'),
)
