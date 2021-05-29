from django.shortcuts import render
from django.views.generic.base import TemplateView  

# Wedding頁
class PortfolioPage(TemplateView):
	template_name = 'portfolio/portfolio.html'

class Portfolio2Page(TemplateView):
	template_name = 'portfolio/portfolio2.html'