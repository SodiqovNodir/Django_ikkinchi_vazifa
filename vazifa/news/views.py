from django.shortcuts import render

def home(request):
    return render(request, 'tillar.html')

def tabiat(request):
    return render(request, 'tabiat.html')

def jadval(request):
    return render(request, 'jadval.html')

def kurs(request):
    return render(request, 'kurs.html')

def harif(request):
    return render(request, 'harif.html')

def elon(request):
    return render(request, 'elon.html')

def malumot(request):
    return render(request, 'malumot.html')

def animation(request):
    return render(request, 'animatsiya.html')

def efect(request):
    return render(request, 'efect.html')

def animation2(request):
    return render(request, 'animation2.html')