from django.shortcuts import render , redirect
import datetime
import random
def index(request):
    try:
        request.session['gold']
    except KeyError:
        request.session['gold'] = 0
    try:
        request.session['activities']
    except KeyError:
        request.session['activities'] = []
    return render(request, 'ninjagold.html')

def process(request):
    if request.method == "POST":
        if request.POST['action'] == "farm":
            earnings = random.randint(10, 20)
            request.session['gold'] += earnings
            request.session['activities'].append('Earned ' + str(earnings) + ' gold from the farm! (' +'{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now()))
            
            return redirect('/')
        
        elif request.POST['action'] == "cave":
            earnings = random.randrange(5, 10)
            request.session['gold'] += earnings
            request.session['activities'].append('Earned ' + str(earnings) + ' gold from the cave! (' +'{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now()))
            return redirect('/')
        
        elif request.POST['action'] == "house":
            earnings = random.randrange(2, 5)
            request.session['gold'] += earnings
            request.session['activities'].append(
                'Earned ' + str(earnings) + ' gold from the house! (' +
                '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now()))
            return redirect('/')
        
        elif request.POST['action'] == "casino":
            earnings = random.randrange(-50, 50)
            request.session['gold'] += earnings
            if earnings > 0:
                request.session['activities'].append(
                    'Entered a casino and Won ' + str(earnings) + ' gold! (' +'{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now()))
                return redirect('/')
            
            else:
                request.session['activities'].append(
                    'Entered a casino and Lost ' + str(earnings) + ' gold. Ouch! (' +
                    '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now()))
                return redirect('/')
    else:
        return redirect('/')

def reset(request):
    request.session['gold'] = 0
    request.session['activities'] = []
    return render(request, 'ninjagold.html')
