from django.shortcuts import render
from django.db.models import Q
from products.models import Marque,Model
from accounts.models import Client
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect
# Create your views here.

def Index(request):
    models = Model.objects.select_related('id_marque').all()[:6]
    marques = Marque.objects.all()
    context = {
    'models': models,
    'marques': marques,
    }
    return render(request, 'index.html', context)
def logout(request):
    if 'user' in request.session:
        del request.session['user']
    return redirect('Index')

def car(request, car):
        model = Model.objects.get(nom=car)
        if request.method == 'POST':
            cin = request.POST.get('CIN')
            prenom = request.POST.get('FirstName')
            nom = request.POST.get('LastName')
            email =  request.POST.get('Email')
            sexe = request.POST.get('Sex')
            date = request.POST.get('ReservationDate')
            phone = request.POST.get('Phone')
            if sexe == 'male':
                sexe = 'male'
            else:
                sexe = 'female'
            try:
                client = Client.objects.create(
                        cin=cin,
                        prenom=prenom,
                        nom=nom,
                        email=email,
                        sexe=sexe,
                        Reservation_Date=date,
                        telephone=phone,
                        ModelName=model,
                    )
                client.save()
                context = {'model': model,'car':car}
                return redirect('Index')
            except Client.DoesNotExist:
                error = "error"
                context = {'model': model,'car':car,'error':error}
                return render(request, 'pages/car.html', context)
        else:
            context = {'model': model,'car':car}
            return render(request, 'pages/car.html', context)

def model(request, make):
    marque = Marque.objects.get(nom=make)
    models = Model.objects.filter(id_marque=marque.id_marque)
    context = {'models': models,'make':make}
    return render(request, 'pages/model.html', context)

def models(request):
    marques = Marque.objects.all()
    context = {'marques': marques,}
    return render(request, 'pages/models.html', context)

def search(request):
    car = request.GET.get('car')
    pay = request.GET.get('pay')
    year = request.GET.get('year')
    text_car = "marque: "+car if car else ""
    text_pay = ", payment: "+pay if pay else ""
    text_year = ", year: "+year if year else ""
    try:
        marque = Marque.objects.get(nom__icontains=car)
        result = Model.objects.filter(id_marque=marque.id_marque,price__lt=pay,annee__lt=int(year)+1)
        other = Model.objects.filter(~Q(id_marque=marque.id_marque) & Q(price__lt=pay) & Q(annee__lt=int(year)+1))[:3]
        if marque is not None:
            error = "No results found for"
            context = {'result':result,
                    'text_car':text_car,
                    'text_pay':text_pay,
                    'text_year':text_year,
                    'error':error,
                    'other':other,}
            return render(request, 'pages/search.html', context)
        else:
            error = "marque is not found for"
            context = {'error':error,
                        'text_car':text_car,}
            return render(request, 'pages/search.html', context)
    except Marque.DoesNotExist:
        error = "No results found for"
        context = {'error':error,
                   'text_car':text_car,
                    'text_pay':text_pay,
                    'text_year':text_year,}
        return render(request, 'pages/search.html', context)

def page404(request, exception):
    return render(request, 'pages/404.html', status=404)
