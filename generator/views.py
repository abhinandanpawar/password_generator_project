from django.shortcuts import render
# Create your views here.
import random

def home(request):
    return render(request,'generator/home.html')


def password(request):
    characters =list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('numbers'):
        characters.extend('0123456789')
    if request.GET.get('special'):
        characters.extend('<>?"[]-!@$#%(#_%($)')
    pas=''
    length=int(request.GET.get('length'))
    for i in range(length):
        pas +=random.choice(characters)
    return render(request,'generator/password.html',{'password':pas})

def about(request):
    return render(request,'generator/about.html')