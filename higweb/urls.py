from django.conf.urls import patterns, include, url
from django.contrib import admin
from web.api import EntryResource

entry_resource = EntryResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'higweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(entry_resource.urls)),
    url(r'^web/', include('web.urls')),
)
