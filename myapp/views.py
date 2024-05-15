from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm

people = []

def add_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            person = Person(username=username, password=password)
            person.save()
            people.append(person)
            return redirect('show_people')
    else:
        form = PersonForm()
    return render(request, 'add_person.html', {'form': form})

def show_people(request):
    people = Person.objects.all()
    return render(request, 'show_people.html', {'people': people})
