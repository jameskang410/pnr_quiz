from django.shortcuts import render

from rest_framework import generics
from pnr_quiz_site.models import PnrQuotes
from pnr_quiz_site.serializers import PnrQuotesSerializer, CreatePnrQuotesSerializer

from django.core.mail import send_mail

# Create your views here.

class QuotesList(generics.ListAPIView):
    """
    Lists all quotes for API
    For my own use. Should probably be disabled later.
    """
    queryset = PnrQuotes.objects.all()
    model = PnrQuotes
    serializer_class = PnrQuotesSerializer

class PersonList(generics.ListAPIView):
    """
    Lists all unique people
    Used for creating a dropdown of all possible choices
    """

    queryset = PnrQuotes.objects.values('person').order_by('person').distinct()
    model = PnrQuotes
    serializer_class = PnrQuotesSerializer

class QuizList(generics.ListAPIView):
    """
    Chooses 10 random quotes for API
    """
    queryset = PnrQuotes.objects.all().order_by('?')[:10]
    model = PnrQuotes
    serializer_class = PnrQuotesSerializer

class QuotesAdd(generics.CreateAPIView):
    """
    Add new quotes for API
    """
    model = PnrQuotes
    serializer_class = CreatePnrQuotesSerializer

    # changing up the save method to do some validations on the data
    def perform_create(self, serializer):

        try:
            person = serializer.validated_data['person']
            quote = serializer.validated_data['quote']

            #cleaning - strip, capitalize first letter, remove period
            quote = quote.strip()
            quote = quote[0].upper() + quote[1:]
            quote = quote.rstrip('.')

            #if the length is 160 or less
            if len(quote) < 161:

                serializer.save(person=person, quote=quote)

                #email notification
                email_message = 'The following quote was added:\nPerson: %s\nQuote: %s' % (person, quote)
                send_mail(subject='Quote Added', message=email_message, from_email='parksandrecquiz@gmail.com', recipient_list=['jameskang410@gmail.com'], 
                            fail_silently=False)




        except:

            pass

def home(request):
    """
    View for home
    """

    return render(request, 'home/index.html')