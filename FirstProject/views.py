from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    return HttpResponse('Hi. This is about page')

def mainpage(request):
    return render (request, 'home.html')

def reverse(request):
    user_text = request.GET['usertext']
    reversed_text = user_text[::-1]
    res = len(user_text.split())
    return render (request, 'reverse.html', {'usertext':user_text, 'reversetext':reversed_text, 'num_words': str(res)})    