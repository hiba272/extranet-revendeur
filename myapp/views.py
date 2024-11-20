from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Facture 
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Hi {user.username}, your account was created successfully.')
            return redirect('login')
        else:
            messages.error(request, "There was an error with your registration.")
            messages.error(request, "Or maybe a username already exists.")
            
    else:
        form = CustomUserCreationForm()
    return render(request, 'myapp/signup.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('user_interface')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'myapp/login.html', {'form': form})
@login_required
def user_interface_view(request):
    # Récupérer toutes les factures de la base de données
    factures = Facture.objects.all()

    # Passer les factures au template
    context = {
        'factures': factures
    }
    
    return render(request, 'myapp/user_interface.html', context)
def facture_detail_view(request, facture_id):
    # Récupérer la facture spécifique ou renvoyer une 404 si elle n'existe pas
    facture = get_object_or_404(Facture, id=facture_id)
    
    # Passer les détails de la facture au template
    context = {
        'facture': facture
    }
    
    return render(request, 'myapp/facture_detail.html', context)
@login_required
def generer_recu(request, facture_id):
    facture = get_object_or_404(Facture, id=facture_id)

   
    date_validation = timezone.now()

    facture.delete()
    proprietaire_cheque = request.GET.get('proprietaire_cheque', facture.proprietaire_cheque)


    # Créer le contexte pour le reçu
    context = {
        'facture': facture,
        'revendeur': request.user,  # Assurez-vous que l'utilisateur est connecté
        'date_validation': date_validation,
        'proprietaire_cheque': proprietaire_cheque,
    }

    # Rendre le template du reçu
    return render(request, 'myapp/generer_recu.html', context)
