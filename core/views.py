from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from core.models import producto


class Inicio(TemplateView):
    template_name = 'Cliente/index.html'
    page_title = 'Inicio'
    
    def get_context_data(self, **kwargs):
        context = super(Inicio, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['producto'] = producto.objects.all()
        return context

class Crearproducto(TemplateView):
    template_name = 'Cliente/crear_producto.html'
    page_title = 'Crear producto'
    
    def get_context_data(self, **kwargs):
        context = super(Crearproducto, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        return context