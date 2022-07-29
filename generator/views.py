from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')
def password(request):
    # a list of char to put in passwword 
    characters = list('abcdefghjiklmnopqrstuvwyz')
    # if user want a specific pass combination
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWYZ'))
    if request.GET.get('Special Characters'):
        characters.extend(list('!@#$%&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    # the pass length.
    # the GET gets the requested pass length
    # The number 13 is the default pass length
    length = int(request.GET.get('length',13))
    # the pass first to  be an empty string
    thepassword = ''
    # iterate through  our list
    for x in range(length):
        # generate a random pass by also adding a char in each iteration
        thepassword += random.choice(characters)
    return render(request, 'generator/password.html', {'password':thepassword})

def about(request):
    return render(request, 'generator/about.html')