from django.urls import path

from .views import PruebaView, PruebaListView

urlpatterns = [
    path('prueba/', PruebaView.as_view()),
    path('lista/', PruebaListView.as_view())
]