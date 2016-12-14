from django.shortcuts import render, redirect
from .models import User
import bcrypt
from django.contrib import messages

# Create your views here.
def index(request):
    # print User.objects.last().id
    return render(request, 'loginRegApp/index.html')
def register(request):
    postData = {
        'f_name': request.POST['first_name'],
        'l_name': request.POST['last_name'],
        'email': request.POST['email'],
        'password': request.POST['password'],
        'c_password': request.POST['confirm_password']
    }

    user = User.objects.validate(postData)

    if user[0]:
        for error in user[1].itervalues():
            messages.error(request, error)
    else:
        request.session['id'] = User.objects.last().id
        user = User.objects.last()
        context = {'user': user}
        return render(request, "loginRegApp/loggedin.html", context)

    return redirect('/')

def login(request):
    user = User.objects.filter(email = request.POST['email']) # got the user from the DB, it's a user object in a list.

    if user:
        if bcrypt.hashpw(request.POST['password'].encode('utf-8'), user[0].password.encode('utf-8')) == user[0].password:
            request.session['id'] = user[0].id
            context = {'user': user[0]}
            return render(request, "loginRegApp/loggedin.html", context)
        else:
            messages.error(request, "This is not the correct username or password")
            return redirect('/')
    else:
        messages.error(request, "This is not the correct username or password")
        return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')
