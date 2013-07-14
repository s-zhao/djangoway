
from django.conf.urls import url, patterns

urlpatterns = patterns('ajax_demo.views',
    url(r'^$', 'index', name='index'),
    url(r'^contacts/$', 'contacts', name='contacts'),
    url(r'^contact/new/$', 'contact_new', name='contact-new'),
    url(r'^contact/contact/save/$', 'contact_save_new', name='contact-save-new'),
    url(r'^contact/(?P<pk>\d+)/$', 'contact_details', name='contact-details'),
    url(r'^contact/(?P<pk>\d+)/edit/$', 'contact_edit', name='contact-edit'),
    url(r'^contact/save$', 'contact_save_edit', name='contact-save'),
    

)

