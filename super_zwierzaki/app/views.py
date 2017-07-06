from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User

from social_django.models import UserSocialAuth

from django.http import HttpResponse
from django.template import loader
from django.utils import timezone

from .models import Card
from .forms import CardForm
from .forms import SignUpForm


@login_required
def index(request):
    card_list = Card.objects.all()
    template = loader.get_template('app/index.html')
    context = {
        'card_list' : card_list,
    }
    return HttpResponse(template.render(context, request))

@login_required
def card_new(request):
    if request.method == "POST":
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.owner = request.user
            card.added_date = timezone.now()
            card.save()
            return redirect('index')
    else:
        form = CardForm()
    return render(request, 'app/card_edit.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'app/signup.html', {'form': form})

@login_required
def settings(request):
    user = request.user

    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, 'app/settings.html', {
        'facebook_login': facebook_login,
        'can_disconnect': can_disconnect
    })


@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Hasło zostało zmienione!')
            return redirect('password')
        else:
            messages.error(request, 'Proszę poprawić błąd.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'app/password.html', {'form': form})
