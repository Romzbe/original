from django.shortcuts import render

def index(request):
    data={
        'title':'glllllava',
        'values':['y',"sd",'1234'],

    }

    return render(request,"popo/index.html", data )

def about(request):
    return render(request,"popo/about.html")