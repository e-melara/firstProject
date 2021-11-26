from django.urls import path


def DesdeApps(self):
    print("Desde la app de persona")

    
urlpatterns = [
    path('persona/', DesdeApps)
]