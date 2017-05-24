from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader

from .models import Card

def index(request):
    cards_list = Card.objects.all()
    template = loader.get_template('app/index.html')
    context = {
        'cards_list' : cards_list,
    }
    return HttpResponse(template.render(context, request))
