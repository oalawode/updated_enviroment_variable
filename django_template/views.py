from django.shortcuts import render


def home_view(request,id =1):
    return render(request,"home.html"
    )
