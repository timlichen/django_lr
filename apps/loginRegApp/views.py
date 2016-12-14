from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
    print User.objects.last().id
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
