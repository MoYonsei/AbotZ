# bots/views.py
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy, reverse
from .models import Bot, BotAction
from django.conf import settings
from .forms import BotForm, BotActionForm
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BotActionSerializer
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .bluestacks_control import install_app, launch_app, stop_app



class BotsListView(LoginRequiredMixin, ListView):
    model = Bot
    template_name = 'bots/bots_list.html'
    context_object_name = 'bots'
    login_url = reverse_lazy('user_accounts:login')  
    redirect_field_name = 'bots/bots_list' 

    def get_queryset(self):
        return Bot.objects.filter(owner=self.request.user)


class CreateBotView(LoginRequiredMixin, CreateView):
    model = Bot
    form_class = BotForm
    template_name = 'bots/create_bot.html'
    login_url = reverse_lazy('user_accounts:login')  

    def form_valid(self, form):
        form.instance.owner = self.request.user
        response = super().form_valid(form)
        bot_id = self.object.id 
        self.success_url = reverse('bots:bot_controller', args=[bot_id])
        return response



class BotControllerView(LoginRequiredMixin, DetailView):
    model = Bot
    template_name = 'bots/bot_controller.html'
    context_object_name = 'bot'
    login_url = reverse_lazy('user_accounts:login') 
    redirect_field_name = 'bots/bots_list' 

    def get_object(self):
        bot = super().get_object()
        if bot.owner != self.request.user:
            raise PermissionDenied("You are not allowed to access this bot.")
        return bot

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        bot_id = self.object.id
        action = request.POST.get('action')
        app_path = request.POST.get('app_path')
        package_name = request.POST.get('package_name')

        try:
            if action == 'install':
                stdout, stderr = install_app(self.object.emulator_id, app_path)
            elif action == 'launch':
                stdout, stderr = launch_app(self.object.emulator_id, package_name)
            elif action == 'stop':
                stdout, stderr = stop_app(self.object.emulator_id, package_name)
            else:
                return JsonResponse({"error": "Invalid action"}, status=400)

            if stderr:
                return JsonResponse({"error": stderr}, status=500)
            return JsonResponse({"stdout": stdout}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)



class ActionCreateView(CreateView):
    model = BotAction
    form_class = BotActionForm
    template_name = 'bots/action_form.html'
    success_url = reverse_lazy('bots:bots_list')

class ActionUpdateView(UpdateView):
    model = BotAction
    form_class = BotActionForm
    template_name = 'bots/action_form.html'
    success_url = reverse_lazy('bots:bots_list')

class ActionDeleteView(DeleteView):
    model = BotAction
    success_url = reverse_lazy('bots:bots_list')


class SaveActionsView(APIView):
    def post(self, request, format=None):
        serializer = BotActionSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    





class UpdateBotView(UpdateView):
    model = Bot
    form_class = BotForm
    template_name = 'bots/edit_bot.html'
    success_url = reverse_lazy('bots:list_bots')

class DeleteBotView(DeleteView):
    model = Bot
    success_url = reverse_lazy('bots:list_bots')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return JsonResponse({'success': True})
    



def custom_error_view(request, exception=None):
    return render(request, 'bots/error.html', {'message': 'You do not have permission to access this page or the page does not exist.'})


