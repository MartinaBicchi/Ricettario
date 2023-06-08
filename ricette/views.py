from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Ricetta, Categoria, Commento, Preferiti
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import login, authenticate, logout
from .forms import FormNuovaRicetta, FormCommento
from itertools import groupby


# Create your views here.

def ricettehome(request):
    return render(request, 'Home.html') #la funzione render, già importata, possiamo renderizzare una pagina web. prende in ingresso requeste e una stringa che indica la pagina web da visualizzare

def iscrizione(request):
    return render(request, 'Iscriviti.html')

def Login(request):
    return render(request, 'Login.html')

def accedi(request):
    ricette = Ricetta.objects.order_by('categoria')
    gruppi = groupby(ricette, lambda x: x.categoria)
    gruppi = [(categoria, list(ricette)) for categoria, ricette in gruppi]
    context = {'gruppi': gruppi}
    return render(request, 'Accedi.html', context)

def bottoneCreaRicetta(request):
    context = {
        'categorie': Categoria.CATEGORIE,
    }
    return render(request,'CreaRicetta.html', context)


def Userlogout(request):
    logout(request)
    redirect('ricettehome')

def ricettadescrizione(request, id_ricetta):
    ricetta = get_object_or_404(Ricetta, pk=id_ricetta)
    nome=ricetta.titolo
    comments = Commento.objects.filter(Ricetta__titolo=nome)
    context = {
        'ricetta': ricetta,
        'comments': comments
    }
    return render(request, 'DescrizioneRicetta.html', context)

def preferiti(request):
    preferiti = Preferiti.objects.filter(Utente=request.user)
    context = {'preferiti': preferiti}
    return render(request, 'Preferiti.html', context)


def register(request):
    if request.method == 'POST' and request.POST.get('Password') == request.POST.get('Password1'):
        username = request.POST. get('NomeUtente')
        name=request.POST.get('Nome')
        cognome = request.POST.get('Cognome')
        email = request.POST. get('IndirizzoEmail')
        password = request.POST.get('Password')
        if User.objects.filter(username=username).exists():
            return redirect('HOME')
        user = User.objects.create_user(username=username, first_name= name, last_name=cognome, email=email, password=password)
        content_type = ContentType.objects.get_for_model(Ricetta)
        permission = Permission.objects.get(
            content_type=content_type,
            codename='add_ricetta'
        )
        user.user_permissions.add(permission)
        return redirect('login')
    else:
        return render(request, 'Iscriviti.html')

def create_ricetta(request):
    if request.method=='POST':
        form=FormNuovaRicetta(request.POST)
        if form.is_valid():
            ricetta=form.save(commit=False)
            categoria_nome=form.cleaned_data['categoria']
            try:
                categoria = Categoria.objects.get(nome=categoria_nome)
                ricetta.categoria=categoria
                ricetta.save()
                return redirect('accedi')
            except Categoria.DoesNotExist:
                form.add_error('categoria', 'Seleziona una categoria valida')
        else:
            print(form.errors)
    else:
        form=FormNuovaRicetta()

    context={
        'form': form,
        'categorie': Categoria.CATEGORIE,
    }
    return render(request, 'CreaRicetta.html', context)


def registerLogin(request):
    user1 = request.POST.get('NomeUtente')
    email1 = request.POST.get('IndirizzoEmail')
    pass1 = request.POST.get('Password')
    user = authenticate(username=user1, email=email1, password=pass1)
    if user is not None:
       login(request, user) # Continua con il flusso normale
       return redirect('accedi')
    else:
        return redirect('HOME')


@login_required
def AddCommento(request, id_recipes):
    if request.method=='POST':
        form=FormCommento(request.POST)
        if form.is_valid():
            commento=form.save(commit=False)
            try:
                ricetta = Ricetta.objects.get(id=id_recipes)
                commento.Ricetta=ricetta
                commento.Utente=request.user
                commento.save()
                return redirect('ricettadescrizione', id_recipes)
            except Ricetta.DoesNotExist:
                form.add_error('Ricetta', 'Seleziona una Ricetta valida')
        else:
            print(form.errors)
    else:
        form=FormCommento()

    context={
        'form': form,
        'ricetta': Ricetta.objects.get(id=id_recipes),
        'utente': request.user,
    }
    return render(request, 'Aggiungi_Commento.html', context)


def add_to_favorites(request, recipe_id):
    user = request.user
    recipe = Ricetta.objects.get(id=recipe_id)
    if not Preferiti.objects.filter(Utente=user, Ricetta=recipe).exists():
        preferito = Preferiti.objects.create(Utente=user, Ricetta=recipe)
        preferito.save()
    return redirect('preferiti')

def cercaRicetta(request):
    if request.method == 'POST':
        nome_ricetta = request.POST.get('titolo')
        try:
            ricetta = Ricetta.objects.get(titolo=nome_ricetta)
            return redirect('ricettadescrizione', ricetta.id)
        except Ricetta.DoesNotExist:
            return render(request, 'RicettaNonPresente.html')
    else:
        return redirect('accedi')

def cercaRicettaperCategoria(request):
    if request.method == 'POST':
        categoria_ricetta = request.POST.get('categoria')
        try:
            categoria = Categoria.objects.get(nome=categoria_ricetta)
            ricette = Ricetta.objects.filter(categoria=categoria)
            gruppi = groupby(ricette, lambda x: x.categoria)
            gruppi = [(categoria, list(ricette)) for categoria, ricette in gruppi]
        except Categoria.DoesNotExist:
            return redirect('accedi')

    context = {
        'gruppi': gruppi
    }
    return render(request, 'Accedi.html', context)
