from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponse
from django.template import loader
from django.utils import timezone

from .models import Card
from .forms import CardForm

def index(request):
    cards_list = Card.objects.all()
    template = loader.get_template('app/index.html')
    context = {
        'cards_list' : cards_list,
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
            return redirect('ok')
    else:
        form = CardForm()
    return render(request, 'app/card_edit.html', {'form': form})
