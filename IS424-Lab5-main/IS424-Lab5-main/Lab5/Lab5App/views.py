class Person:
    def __init__(self, name, password):
        self.name = name
        self.password = password

from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.

class Person_Form(forms.Form):
    name = forms.CharField(label="Name")
    password = forms.CharField(label="Password", widget=forms.PasswordInput())

people = []

def add(request):
    if request.method == "POST":
        form = Person_Form(request.POST)

        if form.is_valid():

            name = form.cleaned_data["name"]
            password = form.cleaned_data["password"]

            person = Person(name, password)

            people.append(person)
            return HttpResponseRedirect(reverse("Lab5App:default"))
        else:
            return render(request, "Lab5App/add.html", {"form":form})
    else:
        return render(request, "Lab5App/add.html", {"form": Person_Form})

def default(request):
    return render(request, "Lab5App/default.html", {"people":people})
