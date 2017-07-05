from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

from django.http import HttpResponse
from django.template import loader
from django.utils import timezone

from .models import Card
from .forms import CardForm

def index(request):
    card_list = Card.objects.all()
    template = loader.get_template('app/index.html')
    context = {
        'card_list' : card_list,
    }
    return HttpResponse(template.render(context, request))

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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'app/signup.html', {'form': form})
