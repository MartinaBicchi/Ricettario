from django.contrib import admin
from .models import Ricetta
from .models import Preferiti
from .models import Categoria
from .models import Commento

# Register your models here. #serve per far si che nella pagina del superutente siano disponibili i modelli che creo in models.py
admin.site.register(Ricetta)
admin.site.register(Preferiti)
admin.site.register(Categoria)
admin.site.register(Commento)