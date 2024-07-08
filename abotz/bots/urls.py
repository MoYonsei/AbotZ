# bots/urls.py
from django.urls import path
from .views import BotsListView

app_name = 'bots'

urlpatterns = [
    path('list/', BotsListView.as_view(), name='bots_list'),  # تأكد من أن المسار معرف بشكل صحيح
]
