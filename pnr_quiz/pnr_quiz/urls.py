from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pnr_quiz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # I actually don't know if pointing to the same view is dangerous haha
    # Seems like it's okay
    url(r'^$', 'pnr_quiz_site.views.home', name='home'),
    url(r'^home/', 'pnr_quiz_site.views.home', name='home'),
)
