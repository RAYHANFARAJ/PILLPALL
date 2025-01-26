from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import render

User = get_user_model()

def home(request):
    print("La vue 'home' a été appelée")
    return render(request, 'home.html')


@login_required
def home_authenticated(request):
    return render(request, 'home_authenticated.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def add_medicine(request):
    return render(request, 'add_medicine.html')

@login_required
def medicine_list(request):
    medicines = [
        {"name": "Paracétamol", "quantity": 20},
        {"name": "Ibuprofène", "quantity": 15},
    ]
    return render(request, 'medicine_list.html', {'medicines': medicines})

@login_required
def dispense_medicine(request):
    return render(request, 'dispense_medicine.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_authenticated')  # Redirection vers le tableau de bord
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    return render(request, 'login.html')


def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        is_doctor = request.POST.get('is_doctor') == 'yes'

        if User.objects.filter(username=username).exists():
            messages.error(request, "Nom d'utilisateur déjà pris.")
            return render(request, 'signup.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Cet email est déjà utilisé.")
            return render(request, 'signup.html')

        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            if hasattr(user, 'is_doctor'):
                user.is_doctor = is_doctor
            user.save()
            login(request, user)
            messages.success(request, "Inscription réussie !")
            return redirect('home_authenticated')
        except Exception as e:
            messages.error(request, f"Une erreur est survenue : {e}")
    return render(request, 'signup.html')
def etat_eau(request):
    return render(request, 'etat_eau.html')
def test_view(request):
    print("La vue test_view a été appelée.")  # Cette ligne doit apparaître dans la console
    return render(request, 'test.html')
