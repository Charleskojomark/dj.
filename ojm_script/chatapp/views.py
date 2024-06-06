from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
import json
from pusher import Pusher
from django.conf import settings
import logging
from .models import Conversation, Message
from userauth.models import User

pusher = Pusher(
    app_id=settings.PUSHER_APP_ID,
    key=settings.PUSHER_KEY,
    secret=settings.PUSHER_SECRET,
    cluster=settings.PUSHER_CLUSTER,
    ssl=True
)
logger = logging.getLogger(__name__)

@login_required
def chat(request, username):
    other_user = get_object_or_404(User, username=username)
    conversation = Conversation.objects.filter(participants=request.user).filter(participants=other_user).first()
    if not conversation:
        conversation = Conversation.objects.create()
        conversation.participants.set([request.user, other_user])

    return render_conversation(request, conversation)

@login_required
def chat_conversation(request, conversation_id):
    conversation = get_object_or_404(Conversation, conversation_id=conversation_id)
    if request.user not in conversation.participants.all():
        return HttpResponseForbidden("You are not a participant of this conversation.")

    return render_conversation(request, conversation)

def render_conversation(request, conversation):
    messages = conversation.messages.all()
    other_user = conversation.participants.exclude(id=request.user.id).first()

    context = {
        'conversation': conversation, 
        'messages': messages, 
        'other_user': other_user
    }
    return render(request, 'chat.html', context)

@csrf_exempt
@login_required
def send(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            content = data.get('content')
            conversation_id = data.get('conversation_id')
            sender = request.user

            conversation = get_object_or_404(Conversation, conversation_id=conversation_id)
            message = Message.objects.create(sender=sender, content=content, conversation=conversation)

            pusher.trigger('new-channel', 'new-message', {
                'sender': message.sender.username,
                'content': message.content,
                'conversation_id': conversation.conversation_id
            })

            return JsonResponse({'status': 'success', 'message': 'Message sent'}, status=200)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

@login_required
def my_messages(request):
    user = request.user
    conversations = Conversation.objects.filter(participants=user)
    conversations_with_participants = []

    for conversation in conversations:
        other_user = conversation.participants.exclude(id=request.user.id).first()
        conversations_with_participants.append((conversation, other_user))

    context = {
        'conversations_with_participants': conversations_with_participants
    }
    return render(request, 'messages.html', context)
