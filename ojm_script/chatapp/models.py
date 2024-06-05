from django.utils.crypto import get_random_string
from django.db import models
import hashlib
from userauth.models import User


def generate_random_conversation_id():
    from .models import Conversation  # Importing Conversation model here
    while True:
        random_id = get_random_string(10)  # Adjust the length as needed
        if not Conversation.objects.filter(conversation_id=random_id).exists():
            return random_id

class Conversation(models.Model):
    participants = models.ManyToManyField(User, related_name='conversations')
    conversation_id = models.CharField(max_length=100, default=generate_random_conversation_id, unique=True)

    def save(self, *args, **kwargs):
        if not self.conversation_id:
            # Generate a new conversation ID based on participant IDs if not provided
            participant_ids = sorted([str(participant.id) for participant in self.participants.all()])
            concatenated_ids = '-'.join(participant_ids)
            self.conversation_id = hashlib.sha256(concatenated_ids.encode()).hexdigest()
        super().save(*args, **kwargs)        
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    timestamp = models.DateTimeField(auto_now_add=True)