from django.shortcuts import render

from rest_framework import generics
from pnr_quiz_site.models import PnrQuotes
from pnr_quiz_site.serializers import PnrQuotesSerializer, CreatePnrQuotesSerializer

# Create your views here.

class QuotesList(generics.ListAPIView):
	"""
	Lists all quotes for API
	"""
	queryset = PnrQuotes.objects.all()
	model = PnrQuotes
	serializer_class = PnrQuotesSerializer

class QuizList(generics.ListAPIView):
	"""
	Chooses 10 random quotes for API
	"""
	queryset = PnrQuotes.objects.all().order_by('?')[:10]
	model = PnrQuotes
	serializer_class = PnrQuotesSerializer

class QuotesDetail(generics.RetrieveAPIView):
	"""
	Lists a specific quote for API
	"""

	lookup_field = 'quotes_key'
	queryset = PnrQuotes.objects.all()
	serializer_class = PnrQuotesSerializer

class QuotesAdd(generics.CreateAPIView):
	"""
	Add new quotes for API
	"""
	queryset = PnrQuotes.objects.all()
	model = PnrQuotes
	serializer_class = CreatePnrQuotesSerializer

def home(request):
	"""
	View for home
	"""

	return render(request, 'home/index.html')