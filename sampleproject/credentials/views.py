from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.shortcuts import redirect

# Create your views here.


def login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user=auth.authenticate(username = username, password = password)

        if user is not None :
            auth.login(request,user)
            return redirect ('/')
        
        else:
            messages.info(request,"Invalid Credentials.")
            return redirect ('login')
        
    return render (request,'login.html')

def register(request):

    if request.method == 'POST':

        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']

        if password == confirmpassword :

            if User.objects.filter(username = username).exists():
                messages.info(request,"Username Taken")
                return redirect('register') #redirect to register page.
            
            elif User.objects.filter(email = email).exists():
                messages.info(request,"Email already Taken")
                return redirect('register')
            
            else:

                user=User.objects.create_user(username = username, first_name = first_name, last_name = last_name , password = password , email = email)

                user.save() #to save user 
                messages.info(request,"User Created.")

                return redirect('login')

        
        else:
            
            # print("Password Not Matching") #if not matched this message will be printed on terminal and no table will be created on the database.

            messages.info(request,"Password Not Matching")
            return redirect('register')
        
        return redirect('/') #because of login now it have no value

    return render(request,"registration.html")


def logout(request):
    auth.logout(request)
    return redirect('/')
