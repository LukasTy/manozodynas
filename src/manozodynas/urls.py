from django.conf.urls import patterns, url
from django.conf import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import *

urlpatterns = patterns('',
    url(r'^$', index_view, name='index'),
    url(r'^random_word/$', random_word_view, name='random_word'),
    url(r'^random_word/(?P<count>\d+)$', random_words_view, name='random_words'),
)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT}),
)
