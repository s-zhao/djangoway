
from django.conf.urls import url, patterns

urlpatterns = patterns('',
    url(r'^$', 'ajax2.views.list_record', name='list-record'),
    url(r'^(?P<pk>\d+)/$', 'ajax2.views.get_record', name='view-record'),
    url(r'^(?P<pk>\d+)/save/$', 'ajax2.views.save_record', name='save-record'),
    url(r'^ng/$', 'ajax2.views.ng_way', name='ng-way'),
    url(r'^ng/blogs/$', 'ajax2.views.blogs', name='ng-blogs'),
)    