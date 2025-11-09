from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .models import Message
from .forms import MessageForm
from django.contrib import messages

class InboxView(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'messaging/inbox.html'
    context_object_name = 'messages'

    def get_queryset(self):
        return Message.objects.filter(recipient=self.request.user).order_by('-sent_at')

class SendMessageView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'messaging/send.html'
    success_url = reverse_lazy('inbox')

    def form_valid(self, form):
        form.instance.sender = self.request.user
        messages.success(self.request, 'Mensaje enviado.')
        return super().form_valid(form)

class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    template_name = 'messaging/message_detail.html'

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        # marcar como leído si eres el destinatario
        if obj.recipient == request.user and not obj.read:
            obj.read = True
            obj.save()
        return super().get(request, *args, **kwargs)
