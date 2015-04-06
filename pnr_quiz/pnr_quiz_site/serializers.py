from rest_framework import serializers
from pnr_quiz_site.models import PnrQuotes

class FormatQuotes(serializers.RelatedField):
    """
    NOT SURE WHERE TO PUT THIS
    """

    def to_representation(self, value):
        """
        Returns quote with ellipsis
        """

        # if quote ends with period
        if value.quote.endswith("."):

            formatted_quote = '...' + value.quote + '..'

        # if quote doesn't end with period
        elif value.quote.endswith('!') or value.quote.endswith('?'):

            formatted_quote = '...' + value.quote + '...'

        # hopefully this means that there is no punctuation
        else:

            formatted_quote = '...' + value.quote + '...'

        return formatted_quote

class PnrQuotesSerializer(serializers.ModelSerializer):

    # formatted_quotes = FormatQuotes(many=True, read_only=True)

    class Meta:
        model = PnrQuotes
        fields = ('person', 'quote' ,'quotes_key')