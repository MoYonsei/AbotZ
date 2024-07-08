# bots/views.py
from django.views.generic import ListView
from .models import Bot

class BotsListView(ListView):
    model = Bot
    template_name = 'bots/bots_list.html'
    context_object_name = 'bots'
