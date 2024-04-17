from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from clients import models
from django.urls import reverse_lazy

class Read(LoginRequiredMixin, ListView):
    model = models.Client
    context_object_name = 'clients'
    template_name = 'clients/ListView.html'

class Create(LoginRequiredMixin, CreateView):
    model = models.Client
    template_name = 'clients/CreateView.html'
    fields = ['first_name', 'last_name', 'birthday', 'phone', 'email']
    success_url = reverse_lazy('listview')

class Update(LoginRequiredMixin, UpdateView):
    model = models.Client
    template_name = 'clients/UpdateView.html'
    fields = ['first_name', 'last_name', 'phone', 'email']
    success_url = reverse_lazy('listview')

class Delete(LoginRequiredMixin, DeleteView):
	model = models.Client
	template_name = 'clients/DeleteView.html'
	success_url = reverse_lazy('listview')

class Details(LoginRequiredMixin, DetailView):
    model = models.Client
    template_name = 'clients/DetailsView.html'
    context_object_name = 'client'