from django.shortcuts import render, redirect
from .models import User
import bcrypt
<<<<<<< HEAD
=======
from django.contrib import messages
>>>>>>> 66e2efd558275a9e996b695afa052b8c89cf1701

# Create your views here.
def index(request):
    # print User.objects.last().id
    return render(request, 'loginRegApp/index.html')
def register(request):
<<<<<<< HEAD
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
=======
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
>>>>>>> 66e2efd558275a9e996b695afa052b8c89cf1701
