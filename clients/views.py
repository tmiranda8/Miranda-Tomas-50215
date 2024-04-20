from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from clients import models, forms
from django.urls import reverse_lazy

class ClientsList(LoginRequiredMixin, ListView):
    model = models.Client
    context_object_name = 'clients'
    template_name = 'clients/clientslist.html'

class ClientDetails(LoginRequiredMixin, DetailView):
    model = models.Client
    context_object_name = 'client'
    template_name = 'clients/clientdetails.html'

class NewClient(LoginRequiredMixin, CreateView):
    model = models.Client
    template_name = 'clients/newclient.html'
    success_url = reverse_lazy('clientslist')
    form_class = forms.NewClient

class EditClient(LoginRequiredMixin, UpdateView):
    model = models.Client
    template_name = 'clients/editclient.html'
    fields = ['first_name', 'last_name', 'phone', 'email']
    success_url = reverse_lazy('clientslist')

class DeleteClient(LoginRequiredMixin, DeleteView):
	model = models.Client
	template_name = 'clients/deleteclient.html'
	success_url = reverse_lazy('clientslist')

