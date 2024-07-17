# bots/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls import handler403, handler404
from . import views

app_name = 'bots'
urlpatterns = [
    path('list/', views.BotsListView.as_view(), name='bots_list'),  # تأكد من أن المسار معرف بشكل صحيح
    path('create_bot/', views.CreateBotView.as_view(), name='create_bot'),
    path('bot_controller/<int:pk>/', views.BotControllerView.as_view(), name='bot_controller'),
    path('actions/add/', views.ActionCreateView.as_view(), name='add_action'),
    path('actions/<int:pk>/update/', views.ActionUpdateView.as_view(), name='update_action'),
    path('actions/<int:pk>/delete/', views.ActionDeleteView.as_view(), name='delete_action'),
    path('api/save_actions/', views.SaveActionsView.as_view(), name='save_actions'),
    path('update_bot/<int:pk>/', views.UpdateBotView.as_view(), name='update_bot'),
    path('delete_bot/<int:pk>/', views.DeleteBotView.as_view(), name='delete_bot'),
    
]

handler403 = 'bots.views.custom_error_view'
handler404 = 'bots.views.custom_error_view'
