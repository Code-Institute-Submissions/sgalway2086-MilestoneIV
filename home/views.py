from django.shortcuts import render

# Create your views here.


def index(request):
    '''
    Access the home page of the site
    '''
    return render(request, 'home/index.html')

