from django.urls import path
from AppTwo import views

urlpatterns = [
	path('', views.signup, name='signup'),
]
