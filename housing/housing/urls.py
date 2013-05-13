from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'guide.views.home', name='home'),
    url(r'^hall/(?P<dorm_slug>[\w\-]+)/$', 'guide.views.detail', name='detail'),
    url(r'^detail/', 'guide.views.detail', name="detail_test"),
    url(r'^admin/', include(admin.site.urls)),
)
