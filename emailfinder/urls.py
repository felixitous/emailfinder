from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'emailfinder.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'emailfinder.views.index'),
    url(r'^email/', 'emailfinder.views.get_name'),
    url(r'^admin/', include(admin.site.urls)),
]
