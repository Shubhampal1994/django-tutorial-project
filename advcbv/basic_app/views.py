from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView
from django.http import HttpResponse
from basic_app import models


# class CBView(View):
# 	def get(self, request):
# 		return HttpResponse('CLASS BASED VIEWS!')


# class IndexView(TemplateView):
# 	template_name = 'index.html'

# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(**kwargs)
# 		context['injectme'] = 'Basic Injections!'
# 		return context


class SchoolListView(ListView):
	model = models.School


class SchoolDetailView(DetailView):
	model = models.School
	template_name = 'basic_app/School_detail.html'


# Test Push VE
