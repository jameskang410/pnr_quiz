from django.db import models

# holds data for the quiz
class PnrQuotes(models.Model):
    """
    Holds people and quotes

    To do: 
        -CREATE TESTS FOR ALL OF THE BELOW
    """

    person = models.CharField(max_length=50, blank=True)
    quote = models.TextField(blank=True)
    quotes_key = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'pnr_quotes'

    def __str__(self):
        """
        Making sure object returns a helpful description
        """

        return "%s - %s - %s" % (self.person, self.quote, self.quotes_key)
    
    def format_quote(self):
        """
        Strips quote
        Capitalizes quote
        Returns quote with ellipsis at the beginning and end of quotes
        """
        import re

        #strip white space
        self.quote = self.quote.strip()

        #capitalize first letter of string
        self.quote = self.quote[0].upper() + self.quote[1:]

        # if quote ends with period
        if self.quote.endswith("."):

            formatted_quote = '...' + self.quote + '..'

        # if quote doesn't end with period
        elif self.quote.endswith('!') or self.quote.endswith('?'):

            formatted_quote = '...' + self.quote + '...'

        # hopefully this means that there is no punctuation
        else:

            formatted_quote = '...' + self.quote + '...'

        return formatted_quote

# holds submitted data from users
class PnrQuotesUser(models.Model):
    """
    Holds users' submissions
    """
    person = models.CharField(max_length=50, blank=True)
    quote = models.TextField(blank=True)
    quotes_key = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'pnr_quotes_user'

    def __str__(self):
        """
        Making sure object returns a helpful description
        """

        return "%s - %s - %s" % (self.person, self.quote, self.quotes_key)