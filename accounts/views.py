from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password, make_password
from .models import User
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def login(request):
    if request.method == 'POST':
        gmail = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(gmail=gmail)
            if check_password(password, user.password):
                request.session['user'] = {'name':user.FirstName}
                return redirect('Index')
            else:
                error = 'Invalid email or password!'
                return render(request, 'accounts/login.html', {'error':error})
        except User.DoesNotExist:
            error = "Invalid login credentials!"
            return render(request, 'accounts/login.html', {'error':error})
    else:
        error = ''
        return render(request, 'accounts/login.html', {'error':error})

def signup(request):
    if request.method == 'POST':
        FirstName = request.POST.get('FirstName')
        LastName = request.POST.get('LastName')
        email =  request.POST.get('email')
        password = request.POST.get('password')
        Comfirm = request.POST.get('Comfirm-Password')
        try:
            User.objects.get(gmail=email)
            error = "This email is already in use."
            return render(request, 'accounts/signup.html', {'error' : error})
        except User.DoesNotExist:
                if password == Comfirm:
                    Password = make_password(password)
                    user = User.objects.create(
                        FirstName=FirstName,
                        LastName=LastName,
                        gmail=email,
                        password=Password
                    )
                    user.save()
                    return redirect('login')
                else:
                    errer = "The password and confirm password do not match."
                    return render(request, 'accounts/signup.html', {'errer' : errer})
    else:
        return render(request, 'accounts/signup.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        
        send_mail(
            name, # title
            message, # message 
            email, # sender if not available, the default or configured value will be used
            [settings.EMAIL_HOST_USER], # recipient email address must be in a list or tuple
            fail_silently=False
        )
        return redirect('Index')
    return render(request, 'accounts/contact.html')
