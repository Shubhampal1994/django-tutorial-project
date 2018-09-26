from django.shortcuts import render
# from django.http import HttpResponse
# from AppTwo.models import UserModel
from .forms import UserForm
# Create your views here.


def index(request):
	context = {'a_var': 'Welcome'}
	return render(request, 'AppTwo/home.html', context)


# def users(request):
# 	user_details = User.objects.order_by('first_name')
# 	my_dict = {'user_details': user_details}
# 	return render(request, 'AppTwo/user.html', context=my_dict)


def signup(request):
	form = UserForm()
	
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print('Error: Form invalid!')


	return render(request, 'AppTwo/signup.html', {'form': form})
