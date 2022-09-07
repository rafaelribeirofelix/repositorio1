from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import NameForm, MyNewForm
from  django import  forms 

def users(request):
    form = MyNewForm()


    if request.method == "POST":
        form = MyNewForm(request.POST)
        if form.is_valid():
            form.save(commit = True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request, 'form_name.html',{'form': form} )


def form_name(request):
    form = NameForm()

    if request.method == 'POST':
        form = NameForm(request.POST)

        if form.is_valid():
            print("Form Validation OK :^)")
            print("Name" + form.cleaned_data['name'])
    return render(request, 'form_name.html', {"form": form})


# Create your views here.
def Hello(request):
    return HttpResponse("Hello World")

def help(request):
    variavel_ajuda = {'variavel_ajuda':"IH AH LÁ EU SOU DO VIEWS.PY IRMÃO!"}
    return render(request, 'help.html', context = variavel_ajuda)

def index(request):
    variavel_index = {'variavel_index':"IH AH LÁ EU SOU DO VIEWS.PY IRMÃO !"}
    return render(request, 'index.html', context = variavel_index)

def calculadora(request):
    variavel_calculadora = {'variavel_calculadora':"IH AH LÁ EU SOU DO VIEWS.PY IRMÃO !"}
    return render(request, 'calculadora.html', context = variavel_calculadora)