from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView as AuthPasswordChangeView
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .forms import SignUpForm, ProfileForm
from .models import Profile
from django.contrib import messages

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')

class SignUpView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Cuenta creada. Ya puedes iniciar sesión.')
        return response

class ProfileView(DetailView):
    model = Profile
    template_name = 'accounts/profile.html'
    pk_url_kwarg = 'pk'

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'accounts/profile_form.html'

    def get_object(self, queryset=None):
        # Solo permitir editar tu propio perfil
        return get_object_or_404(Profile, user=self.request.user)

    def get_success_url(self):
        messages.success(self.request, 'Perfil actualizado.')
        return reverse_lazy('profile', kwargs={'pk': self.request.user.profile.pk})

class PasswordChangeView(LoginRequiredMixin, AuthPasswordChangeView):
    template_name = 'accounts/password_change.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, 'Contraseña cambiada. Vuelve a iniciar sesión.')
        return super().form_valid(form)
