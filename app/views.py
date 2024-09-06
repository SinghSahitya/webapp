from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from random import sample
from datetime import  timedelta
from .models import Gift, Letters
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone



def home(request):
    return render(request, 'app/home.html')

def intro(request):
    return render(request, 'app/intro.html')

def openwhen(request):
    content = list(Letters.objects.all())
    return render(request, 'app/openwhen.html', {'content':content})

def letter(request, letter_id):
    letter = get_object_or_404(Letters, pk=letter_id)
    return render(request, 'app/letter.html', {'letter':letter})


def timeline(request):
    return render(request, 'app/timeline.html')

def hbd(request):
    return render(request, 'app/hbd.html')

def gallery(request):
    return render(request, 'app/gallery.html')



def surprise(request):
 
    gifts = list(Gift.objects.all()[:2])
    Gift.objects.filter(pk__in=[gift.pk for gift in gifts]).delete()

    
    return render(request, 'app/surprise.html', {'gifts': gifts})

@csrf_exempt
def reveal_gift(request):
    if request.method == 'POST' and 'gift_id' in request.POST:
        gift_id = request.POST['gift_id']
        
        try:
            # Retrieve the selected gift from the database
            gift = Gift.objects.get(id=gift_id)
            # Remove the gift from the database
            gift.delete()           
            # Return the gift details as a JSON response
            return JsonResponse({'name': gift.name, 'description': gift.description})
        except Gift.DoesNotExist:
            return JsonResponse({'error': 'Invalid gift ID'})

    return JsonResponse({'error': 'Invalid request'})
