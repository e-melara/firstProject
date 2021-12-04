from django.shortcuts import render
from django.views.generic import TemplateView, ListView


class PruebaView(TemplateView):
    template_name = "home/home.html"


class PruebaListView(ListView):
    queryset = ['1', '10', '20', '28', '30']
    context_object_name = "lista"
    template_name = "home/lista.html"


