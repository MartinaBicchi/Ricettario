from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Categoria(models.Model):
    CATEGORIE = [
        ('Antipasti', 'Antipasti'),
        ('Primi', 'Primi'),
        ('Secondi', 'Secondi'),
        ('Contorni', 'Contorni'),
        ('Dolci', 'Dolci'),
    ]
    nome = models.CharField(max_length=200, choices=CATEGORIE)

    def __str__(self):
        return self.nome

class Ricetta(models.Model):
    titolo=models.CharField(max_length=100)
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE, default=1)
    difficolta=models.IntegerField(default=1)
    tempo_svolgimento=models.CharField(max_length=10)
    numero_persone=models.IntegerField(default=1)
    ingredienti=models.TextField()
    istruzioni=models.TextField()

    def __str__(self):
        return self.titolo

class Preferiti(models.Model):
    Utente = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    Ricetta = models.ForeignKey(Ricetta, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Utente.username} - {self.Ricetta.titolo}"


class Commento(models.Model):
    Utente = models.ForeignKey(User, on_delete=models.CASCADE)
    Ricetta = models.ForeignKey(Ricetta, on_delete=models.CASCADE)
    Testo = models.TextField()

    def __str__(self):
        return f"{self.Utente.username} - {self.Ricetta.titolo}"



#ogni volta che si crea una classe nei modelli va fatta la migrazione usando i comandi 1. python manage.py makemigrations;
# 2.python manage.py migrate del terminale per avvertire django della modfica dek database

#ogni volta che si crea un modello devo importarlo e poi aggiungerlo in admin.py