from django.urls import include, re_path

from . import views

urlpatterns = [
    re_path(r'send_message/$', views.send_message_view, name='send_message_view'),
    re_path(r'send_message_api/(?P<thread_id>\d+)/$', views.send_message_api_view, name='send_message_api_view'),
    re_path(r'chat/(?P<thread_id>\d+)/$', views.chat_view, name='chat_view'),
    re_path(r'accounts/', include('django.contrib.auth.urls')),
    re_path(r'', views.messages_view, name='messages_view'),
]
