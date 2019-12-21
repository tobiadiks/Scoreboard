from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Score
	
class homePageView(ListView):
	template_name='result.html'
	model = Score
# Scores Model