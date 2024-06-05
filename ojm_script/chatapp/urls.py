from django.urls import path 
from . import views
from django.urls import reverse

app_name='chatapp'
urlpatterns = [
    path('<str:username>/', views.chat, name='chat'),
    path('chat/send/', views.send, name='send'),
    path('messages/ ', views.my_messages, name='messages'),
    path('chat/conversation/<str:conversation_id>/', views.chat_conversation, name='chat_conversation'),
]





