# user_accounts/views.py
from django.contrib import messages, auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, RedirectView
from .forms import UserRegistrationForm, UserLoginForm
from .models import CustomUser

class RegisterView(CreateView):
    model = CustomUser
    form_class = UserRegistrationForm
    template_name = 'user_accounts/register.html'
    success_url = '/'

    extra_context = {
        'title': 'Register'
    }

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(self.request, *args, **kwargs)

    def get_success_url(self):
        return self.success_url

    def post(self, request, *args, **kwargs):
        if CustomUser.objects.filter(email=request.POST['email']).exists():
            messages.warning(request, 'This email is already taken')
            return redirect('user_accounts:register')

        user_form = UserRegistrationForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save(commit=False)
            password = user_form.cleaned_data.get("password1")
            user.set_password(password)
            user.save()
            messages.success(request, 'Successfully registered')
            return redirect('bots:bots_list')
        else:
            print(user_form.errors)
            return render(request, 'user_accounts/register.html', {'form': user_form})

class LoginView(FormView):
    form_class = UserLoginForm
    template_name = 'user_accounts/login.html'
    success_url = reverse_lazy('bots:bots_list')  # استخدام reverse_lazy مع اسم المسار الصحيح

    extra_context = {
        'title': 'Login'
    }

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(self.request, *args, **kwargs)

    def get_form_class(self):
        return self.form_class

    def get_success_url(self):
        return reverse_lazy('bots:bots_list')  # استخدام reverse_lazy مع اسم المسار الصحيح

    def form_valid(self, form):
        auth.login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

class LogoutView(RedirectView):
    url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return super(LogoutView, self).get(request, *args, **kwargs)
