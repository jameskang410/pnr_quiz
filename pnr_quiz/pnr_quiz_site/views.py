from django.shortcuts import render

from rest_framework import generics
from pnr_quiz_site.models import PnrQuotes
from pnr_quiz_site.serializers import PnrQuotesSerializer

# Create your views here.

class QuotesList(generics.ListCreateAPIView):
	"""
	Lists all QuotesList for API
	"""
	queryset = PnrQuotes.objects.all()
	model = PnrQuotes
	serializer_class = PnrQuotesSerializer

def home(request):
	"""
	View for home
	"""

	return render(request, 'home/index.html')