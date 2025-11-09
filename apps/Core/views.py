from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Page
from .forms import PageForm

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

class PageListView(ListView):
    model = Page
    template_name = 'core/pages_list.html'
    context_object_name = 'pages'

class PageDetailView(DetailView):
    model = Page
    template_name = 'core/pages_detail.html'

class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    form_class = PageForm
    template_name = 'core/page_form.html'
    success_url = reverse_lazy('pages')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PageUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name = 'core/page_form.html'
    success_url = reverse_lazy('pages')

class PageDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = 'core/confirm_delete.html'
    success_url = reverse_lazy('pages')
