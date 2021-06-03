from django.shortcuts import render, redirect, HttpResponse
import random

from django.shortcuts import render, HttpResponse
def index(request):

    if 'color' not in request.session:
        request.session['color'] = ''

    if 'count' not in request.session:
        request.session['count'] = 0

    if 'results' not in request.session:
        request.session['results'] = ''

    if 'rand' not in request.session: 
        request.session['rand'] = random.randint(1, 100)

    print(request.session['rand'])

    context = {
        'results' : request.session['results'],
        'count' : request.session['count'],
        'color' : request.session['color'],
    }

    return render(request, 'index.html', context)

def guess(request):
    
    request.session['count'] += 1

    if int(request.POST['number']) < request.session['rand']:
        request.session['results'] = "Results were TOO LOW!!"
        request.session['color'] = 'red'

    elif int(request.POST['number']) > request.session['rand']:
        request.session['results'] = "Results were TOO HIGH!!"
        request.session['color'] = 'red'

    else: 
        request.session['results'] = "WINNER WINNER CHICKEN DINNER!!!"
        request.session['color'] = 'green'

    return redirect("/")

def redo(request):
    request.session.clear()
    return redirect('/')