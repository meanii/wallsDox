from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required

from django.contrib import messages

# Create your views here.

def account_view(request, *args, **kwargs):
  
  if request.user.is_authenticated:
    return redirect('/')
    
  if request.method == 'POST':
    if request.POST.get('submit') == 'Sign Up':
      return signup(request)
    elif request.POST.get('submit') == 'Login':
      return login(request)
      
  context = {}
  return render(request, 'account.html', context)

@login_required
def logout_view(request, *args, **kwargs):
  auth.logout(request)
  return redirect('/')

def login(request) -> None:
  username = request.POST['username']
  password = request.POST['password']
  
  user = auth.authenticate(
    username=username,
    password=password
    )
  
  if user is not None:
    auth.login(request, user)
    return redirect('/')
  else:
    messages.info(request, 'you have entered wrong username/password! please be make sure you enter correct username and password.')
    return redirect('/accounts')
    
def signup(request) -> None:
  first_name = request.POST['first_name']
  last_name = request.POST['last_name']
  username = request.POST['username']
  email = request.POST['email']
  password = request.POST['password']
  cpassword = request.POST['cpassword']
  
  if password != cpassword:
    messages.info(request, 'your passwords are not matching correctly!\n make sure you enter same and secure password.')
    return redirect('/accounts')
    
  elif User.objects.filter(username=username).exists():
    messages.info(request, f'{username} is already registered in our database, use another one.')
    return redirect('/accounts')
  
  elif User.objects.filter(email=email).exists():
    messages.info(request, f'{email} this email is already registered in our database.')
    return redirect('/accounts')
    
  else:
    user = User.objects.create_user(
    first_name=first_name,
    last_name=last_name,
    username=username,
    email=email,
    password=password
  )
    user.save()
    print('user created')
    return redirect('/accounts')
