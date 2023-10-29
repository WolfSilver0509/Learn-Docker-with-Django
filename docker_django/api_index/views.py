from django.shortcuts import render
from .models import Citation
import random

def citation_aleatoire(request):
    citations = Citation.objects.all()
    citation = random.choice(citations)
    return render(request, 'api_index/citation.html', {'citation': citation})
