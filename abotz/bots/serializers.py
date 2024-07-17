from rest_framework import serializers
from .models import BotAction

class BotActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotAction
        fields = ['bot', 'action_type', 'coordinates', 'duration', 'start_time', 'end_time']
