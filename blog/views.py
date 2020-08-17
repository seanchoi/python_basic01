from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def new(request):
    return HttpResponse("Placeholder to display a new form to create a new blog")

def create(request):
    return redirect('/')

def show(request, num):
    return HttpResponse("placeholder to display blog number: " + str(num))

def edit(request, num):
    return HttpResponse("placeholder to edit blog: " + str(num))

def destroy(request, num):
    return redirect('/')

def template(request):
    context ={
        "name":"Sean",
        "pets": ["dogs","cats","birds","spiders"]
    }

    return render(request, 'index.html', context)

