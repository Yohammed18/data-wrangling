from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# create a view that will be return by the view
def projects(request):
    return HttpResponse('Here are out products')

def project(request, pk):
    return HttpResponse('SINGLE PROJECT {}'.format(pk))