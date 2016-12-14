from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'loginRegApp/index.html')
def register(request):
    print 'yes'
    return redirect('/')
