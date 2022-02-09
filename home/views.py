from django.shortcuts import render


def index(request):
    '''
    Access the home page of the site
    '''
    return render(request, 'home/index.html')
