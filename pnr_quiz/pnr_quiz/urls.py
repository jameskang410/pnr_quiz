from django.conf.urls import patterns, include, url
from django.contrib import admin

from pnr_quiz_site import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pnr_quiz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # Redirects home
    url(r'^$', 'pnr_quiz_site.views.home', name='home'),
    url(r'^home/', 'pnr_quiz_site.views.home', name='home'),

    url(r'^api/$', views.QuotesList.as_view(), name='quotes_list')
)
