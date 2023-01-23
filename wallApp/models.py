from django.db import models
from datetime import datetime
from loginAndRegApp.models import *

class messages(models.Model):
    Users = models.ForeignKey(User, related_name="users_id", on_delete=models.CASCADE)
    message = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def create_message(request):
        id = int(request.session['userid'])
        user_id = User.objects.get(id=id)
        message = request.POST['message']
        messages.objects.create(message=message, Users=user_id)

    def retrive_last_3_messages():
        return messages.objects.all().order_by('-created_at')[:3]

class comments(models.Model):
    messages = models.ForeignKey(messages, related_name="messages_id", on_delete=models.CASCADE)
    Users = models.ForeignKey(User, related_name="comments_users_id", on_delete=models.CASCADE)
    comment = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def create_comment(request):
        comment = request.POST['comment']
        message_id = int(request.POST['message_id'])
        message_obj = messages.objects.get(id=message_id)
        user_id = int(request.session['userid'])
        user_obj = User.objects.get(id=user_id)
        comments.objects.create(messages=message_obj,Users=user_obj, comment=comment)
    
    def retrive_All_comments():
        return comments.objects.all()