from django.contrib import admin

from .models import Message

# from .forms import AdminChatMessageForm


@admin.register(Message)
class ChatMessageAdmin(admin.ModelAdmin):
    # form = AdminChatMessageForm
    # list_display = ('user','message','updated','created')
    list_display = ('text', 'sender', 'thread', 'datetime')
