from django.http import HttpResponse
from django.shortcuts import render


def adminDashboard(request):
    return render(request, 'app/index.html')
