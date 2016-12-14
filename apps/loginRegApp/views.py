from django.shortcuts import render, redirect
from .models import User
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'loginRegApp/index.html')
def register(request):
    data = {
        'first_name': request.POST['first_name'],
        'last_name': request.POST['last_name'],
        'email': request.POST['email'],
        'password': request.POST['password'],
        'confirm_password': request.POST['confirm_password']
    }
    validate = User.objects.validate(data)
    if validate[0]:
        request.session.clear()
        request.session['warnings'] = validate[1]
        return redirect('/')
    else:
        request.session.clear()
        request.session['user'] = str(validate[1])+" has been added successfully!"
        return redirect('/')
def login(request):
    user = User.objects.login(request.POST['email'], request.POST['password'])
    if user != False:
        if bcrypt.hashpw(request.POST['password'].encode('utf-8'), user.password.encode('utf-8')) == user.password.encode('utf-8'):
            context = {'user':user}
            return render(request, 'loginRegApp/success.html', context)
        else:
            request.session['fail'] = "Please enter a valid password!"
            return redirect('/')
    else:
        request.session['fail'] = "Please enter a registered email"
        return redirect('/')
