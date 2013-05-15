from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^housing/$', 'guide.views.home', name='home'),
    url(r'^housing/$', RedirectView.as_view('url': '/housing/')),
    url(r'^housing/hall/(?P<dorm_slug>[\w\-]+)/$', 'guide.views.detail', name='detail'),
    url(r'^housing/admin/', include(admin.site.urls)),
    url(r'^housing/json/', 'guide.views.get_shapes', name='get_shapes'),
    url(r'^housing/hall_json/(?P<dorm_slug>[\w\-]+)/$', 'guide.views.detail_json', name='detail_json'),
)
