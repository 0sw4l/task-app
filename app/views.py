from django.shortcuts import render
from django.views.generic import ListView, CreateView
from . import models, forms
from django.urls import reverse_lazy
# Create your views here.


def inicio(request):
	context = {
		'nombre': 'oswal'
	}
	return render(request, 'index.html', context)


class InicioView(ListView):
	template_name = 'index.html'
	model = models.Task


class TaskCreateView(CreateView):
	form_class = forms.TaskForm
	template_name = 'form.html'
	success_url = reverse_lazy('inicio')

