"""
URL configuration for Ricettario project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ricette import views

urlpatterns = [ #sono inclusi tutti gli URL accessibili nel sito web
    path('admin/', admin.site.urls),
    path('', views.ricettehome, name='HOME'), #ora l'utente quando va all'indirizzo ricette verrà lanciata la vista ricette che si occuperà di renderizzare la pagina html associata
    path('iscriviti/', views.iscrizione),
    path('login/', views.Login, name='login'),
    path('iscriviti/accedi/', views.register, name='register'),
    path('iscriviti/accedi/paginaAccedi', views.accedi, name='accedi'),
    path('iscriviti/accedi/paginaAccedi/CreaRicetta', views.create_ricetta, name='create_ricetta'),
    path('login/accedi/paginaAccedi/', views.registerLogin, name='registerLogin'),
    path('', views.Userlogout, name='logout'),
    path('iscriviti/accedi/paginaAccedi/<int:id_ricetta>', views.ricettadescrizione, name='ricettadescrizione'),
    path('iscriviti/accedi/paginaAccedi/commento/<int:id_recipes>', views.AddCommento, name='AddCommento'),
    path('iscriviti/accedi/paginaAccedi/Preferiti', views.preferiti, name='preferiti'),
    path('iscriviti/accedi/paginaAccedi/add-to-favorites/<int:recipe_id>/', views.add_to_favorites, name='add-to-favorites'),
    path('iscriviti/accedi/paginaAccedi/ricetta', views.cercaRicetta, name='cercaRicetta'),
    path('iscriviti/accedi/paginaAccedi/ricetta/categoria', views.cercaRicettaperCategoria, name='cercaRicettaperCategoria'),
]
