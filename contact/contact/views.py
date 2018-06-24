from django.http import HttpResponse
from django.shortcuts import render
from .models import Contact_Info
#from django.views.decorators.csrf import csrf_exempt

def index(request):
    #return HttpResponse('index')
    return render(request, 'index.html')


def formSubmission(name, email, wrap, message):
    pass

#@csrf_exempt
def Contact_Info(request):


    name = request.POST['name']
    email = request.POST['email']
    wrap = request.POST['wrap']
    message = request.POST['message']

    contact_info = Contact_Info( name = name , email = email, wrap = wrap, message = message )
    contact_info.save()

    print("Your form is submitted ")

    return render(request, 'index.html')

