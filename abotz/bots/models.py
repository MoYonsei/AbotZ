from django.db import models
from django.conf import settings
from .bluestacks_control import create_emulator
# Create your models here.

class Bot(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bots')
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    emulator_id = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.emulator_id:
            self.emulator_id = create_emulator() 
        super().save(*args, **kwargs)
    

class BotAction(models.Model):
    bot = models.ForeignKey(Bot, related_name='actions', on_delete=models.CASCADE)
    action_type = models.CharField(max_length=100, choices=(('click', 'Click'), ('swipe', 'Swipe')))
    coordinates = models.CharField(max_length=100)  # يمكن استخدام JSON لمرونة أكبر
    duration = models.IntegerField(help_text='Duration in seconds')
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.action_type} at {self.coordinates} for {self.duration}s starting at {self.start_time} end {self.end_time}"


