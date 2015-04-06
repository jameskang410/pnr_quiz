from django.db import models

# Create your models here.
class PnrQuotes(models.Model):
    """
    Holds people and quotes

    To do: 
        -CREATE TESTS FOR ALL OF THE BELOW
        -create a method that strips periods from the end of quotes
        -create a method that capitalizes first and last name
            -maybe also have one that rejects submissions that don't have both names
    """

    person = models.CharField(max_length=50, blank=True)
    quote = models.TextField(blank=True)
    quotes_key = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'pnr_quotes'

    def __str__(self):
        """
        Making sure object returns a helpful description
        """

        return "%s - %s - %s" % (self.person, self.quote, self.quotes_key)
