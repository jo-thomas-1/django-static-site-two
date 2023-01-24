from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.shortcuts import redirect

# Create your views here.

def register(request):
	print('STATUS ::: register view started')
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		conf_password = request.POST['conf_password']

		# validate password and confirm password
		if password == conf_password:
			# check if username already exists
			if User.objects.filter(username=username).exists():
				messages.info(request, "Username " + username + " is already taken")
				return redirect('register')
			# check if email already exists
			elif User.objects.filter(email=email).exists():
				messages.info(request, "Email already registered")
				return redirect('register')
			else:
				user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
				user.save()
				messages.info(request, "Account for " + first_name + " has been registered")
				return redirect('login')
		else:
			messages.info(request, "Password and confirm password fields do no match")
			return redirect('register')

	return render(request, 'register.html')

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(username=username, password=password)
		user.save()

		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			messages.info(request, "Invalid username or password")
			return redirect('login')

	return render(request, 'login.html')

def logout(request):
	auth.logout(request)
	return redirect('/')