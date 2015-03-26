from rest_framework import serializers
from pnr_quiz_site.models import PnrQuotes

class PnrQuotesSerializer(serializers.ModelSerializer):

	class Meta:
		model = PnrQuotes
		fields = ('person','quote','quotes_key')