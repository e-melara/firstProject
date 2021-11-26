from django.urls import path


def DesdeApps(self):
    print('La aplicacion de departamento ya funciona')


urlpatterns = [
    path('departamento/', DesdeApps)
]
