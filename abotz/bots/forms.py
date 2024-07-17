from django import forms
from .models import Bot, BotAction

class BotForm(forms.ModelForm):
    class Meta:
        model = Bot
        fields = ['name', 'description']
        labels = {
            'name': 'Bot Name',
            'description': 'Description',
        }
        widgets = {
            'description': forms.Textarea(attrs={'cols': 40, 'rows': 5}),
        }

class BotActionForm(forms.ModelForm):
    class Meta:
        model = BotAction
        fields = ['action_type', 'coordinates', 'duration', 'start_time', 'end_time']
