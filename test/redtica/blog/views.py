from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Categoria,Entrada

# Create your views here.

"""class IndexView(ListView):

	template_name = 'index.html'
	model = Entrada

class EntradaDetailView(DetailView):
	template_name = 'entrada_detail.html'
	model = Entrada"""

def index(request):
	context = {
		"template_name": "index.html",
	}

	return render(request, "index.html", context)

def post_list(request):
	context = {
		"template_name": "post_list.html",
		"queryset": Entrada.object.all(),
	}

	return render(request, "post_list.html", context)

def post_detail(request, slug=None):
	instance = get_object_or_404(Entrada, slug=slug)
	context = {
		"title": instance.titulo,
		"instance": instance,
	}

	return render(request, "entrada_detail.html", context)

