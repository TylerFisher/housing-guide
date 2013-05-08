from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'guide.views.home', name='home'),
     url(r'^dorm/(?P<dorm_name>[\w\-]+)', 'guide.views.detail', name='detail'),
     url(r'^detail/', 'guide.views.detail', name="detail_test"),
    # url(r'^housing/', include('housing.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
