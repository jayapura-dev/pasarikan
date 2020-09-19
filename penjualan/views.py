from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy

def login(request):
    return render(request,'auth/login.html')


@login_required
def dashboard(request):
    contex = {
        'page_title': 'Dashboard | Admin'
    }

    return render(request,'page/dashboard.html',contex)




