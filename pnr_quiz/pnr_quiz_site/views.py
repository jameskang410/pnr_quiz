from django.shortcuts import render

from rest_framework import generics
from pnr_quiz_site.models import PnrQuotes, PnrQuotesUser
from pnr_quiz_site.serializers import PnrQuotesSerializer, CreatePnrQuotesSerializer

from django.http import JsonResponse
import json

import redis

# used to make salt
import random
import string

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
    model = PnrQuotesUser
    serializer_class = CreatePnrQuotesSerializer

    # changing up the save method to do some validations on the data
    def perform_create(self, serializer):
        r = redis.StrictRedis()

        try:
            person = serializer.validated_data['person']
            quote = serializer.validated_data['quote']

            #cleaning - strip, capitalize first letter, remove period
            quote = quote.strip()
            quote = quote[0].upper() + quote[1:]
            quote = quote.rstrip('.')

            #if the length is 160 or less
            if len(quote) < 161:

                #save to user db
                serializer.save(person=person, quote=quote)

                email_message = 'The following quote was added:\n\n\nPerson: %s\nQuote: %s' % (person, quote)

            else:
                email_message = 'The following quote was NOT added:\n\n\nPerson: %s\nQuote: %s' % (person, quote)

        except Exception as e:

            email_message = 'There was an error with submission. Details below:\n\nPerson: %s\nQuote: %s\n\nError: %s' % (person, quote, e)

        #email notification - push into redis list (will be compiled and e-mailed later by cron)
        r.lpush("pnr_added_quotes", email_message)

def home(request):
    """
    View for home
    """

    return render(request, 'home/index.html')

def submit_score(request):
    """
    Handles user data (POST)
    Returns leaderboard data
    """

    # want to avoid binary strings
    r = redis.StrictRedis(decode_responses=True)


    if request.method == "POST":

        # AngularJS post requires this nonsense
        request_body = json.loads(request.body.decode('ascii'))    

        user_name = request_body["name"]
        user_score = request_body["score"]

        # creating salt - useful for identical usernames - keep distinction
        salt =  ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
        
        salted_user_name = user_name + salt

        # adding to redis
        r.zadd("pnr_scores", user_score, salted_user_name)

        # trimming redis set to top 10 scores
        r.zremrangebyrank("pnr_scores", 0, -10)

        # create python list
        leaders = []

        for user in r.zrange("pnr_scores", 0, -1):
            user_score = r.zscore("pnr_scores", user)

            # get rid of salt on user name
            formatted_user = user[:-5]

            leaders.append({"user": formatted_user, "score": user_score})

        return JsonResponse({"leaders" : leaders})

def leaders(request):
    """
    View leaderboard
    """

    r = redis.StrictRedis(decode_responses=True)

    # create python list
    leaders = []

    for user in r.zrange("pnr_scores", 0, -1):
        user_score = r.zscore("pnr_scores", user)

        # get rid of salt on user name
        formatted_user = user[:-5]

        # insert @ beginning or else list will be upside down
        leaders.insert(0, {"user": formatted_user, "score": user_score})

    return render(request, 'leaders/leaderboard.html', {"leaders" : leaders})