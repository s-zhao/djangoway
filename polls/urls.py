from django.conf.urls import url, patterns

#from polls import views

if 0:
    urlpatterns = patterns('polls.views',
        url(r'^$', 'index', name='index'),
        url(r'^(?P<poll_id>\d+)/$', 'detail', name='detail'),
        url(r'^(?P<poll_id>\d+)/result/$', 'result', name='result'),
        url(r'^(?P<poll_id>\d+)/vote/$', 'vote', name='vote'),    
    )
if 1:
    from polls import views
    urlpatterns = patterns('polls.views',
        url(r'^$', views.IndexView.as_view(), name='index'),
        url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
        url(r'^(?P<pk>\d+)/result/$', views.ResultView.as_view(), name='result'),
        url(r'^(?P<poll_id>\d+)/vote/$', 'vote', name='vote'),    
    )
