from rest_framework import serializers
from pnr_quiz_site.models import PnrQuotes, PnrQuotesUser

class PnrQuotesSerializer(serializers.ModelSerializer):

    class Meta:
        model = PnrQuotes
        fields = ('person', 'format_quote' ,'quotes_key')

class CreatePnrQuotesSerializer(serializers.ModelSerializer):
    """
    This serializer allows users to add quotes to the database.
    It does not include the quotes_key PK field because by 
    omitting it, it'll auto-increment
    """
    class Meta:
        model = PnrQuotesUser
        fields = ('person', 'quote',)