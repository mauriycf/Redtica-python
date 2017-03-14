from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Categoria,Entrada

# Create your views here.

class IndexView(ListView):

	template_name = 'index.html'
	model = Entrada

class EntradaDetailView(DetailView):
	template_name = 'entrada_detail.html'
	model = Entrada