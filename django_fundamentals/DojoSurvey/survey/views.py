from django.shortcuts import render, redirect

def index(request):
    return render(request, 'survey.html')

def result(request):
    name = request.POST['name']
    location = request.POST['location']
    favlanguage = request.POST['favlanguage']
    comment = request.POST['comment']
    context = {
        "name": name,
        "location" : location,
        'favlanguage': favlanguage,
        "comment" : comment
    }
    return render(request, 'result.html' , context)

def back(request):
    return redirect('/')
