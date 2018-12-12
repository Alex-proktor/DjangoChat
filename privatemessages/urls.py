from django.conf.urls import patterns, url
from django.urls import path, include

urlpatterns = patterns('privatemessages.views',
    path('^send_message/$', 'send_message_view'),
    path('^send_message_api/(?P<thread_id>\d+)/$', 'send_message_api_view'),
    path('^chat/(?P<thread_id>\d+)/$', 'chat_view'),
    path('^$', 'messages_view'),
)
