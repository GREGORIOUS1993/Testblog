from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .forms import SignUpForm, EditProfileForm


# Create your views here.



# Login View
def login_user(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, ('You Have Been Logged In!'))
			return redirect('/')
	        
		else:
			messages.success(request, ('Invalid Credentials! Please Try Again'))
			return redirect('login')
	      

	else:
		return render(request, 'login.html', {})



# Logout View
def logout_user(request):
	logout(request)
	messages.success(request, ('You Have Been Logged Out...'))
	return redirect('login')




# Register View
def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(request, username=username, password=password)
			login(request, user)
			messages.success(request, ('You Have successfully Register!'))
			return redirect('post_list')
	else:
		form =SignUpForm()

	context = {'form': form}
	return render(request, 'register.html', context)







def edit_profile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			messages.success(request, ('Your Changes Have Been Saved'))
			return redirect('post_list')
	else:
		form =EditProfileForm(instance=request.user)

	context = {'form': form}
	return render(request, 'profile.html', context)




def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			messages.success(request, ('Password Changed successfully'))
			return redirect('post_list')
	else:
		form =PasswordChangeForm(user=request.user)

	context = {'form': form}
	return render(request, 'password.html', context)