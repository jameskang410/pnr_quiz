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

    # API links
    
    # view all quotes/rows
    url(r'^api/list/$', views.QuotesList.as_view(), name='quotes_list'),
    # post new quote
    url(r'^api/add/$', views.QuotesAdd.as_view(), name='quotes_add'),
    # view 10 random quotes/rows for quiz
    url(r'^api/quiz/$', views.QuizList.as_view(), name='quotes_quiz'),
    # view all distinct persons
    url(r'^api/persons/$', views.PersonList.as_view(), name='persons'),
)
