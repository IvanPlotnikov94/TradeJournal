from django.shortcuts import render
from django.http import HttpResponse


#def index(request):
#    return HttpResponse("<h3>Привет, здесь будет информация по твоим трейдам!</h3>")

def index(request):
    return render(request, 'trades/trades.html')
