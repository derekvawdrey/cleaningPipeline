from .BaseCleaner import BaseCleaner

class UnbalancedQuoteCleaner(BaseCleaner):

    def validate(self, source, target):
        """
        Validate the data.
        """

        # If have double single quotes in the source, return false
        # Double double quotes are handled easier
        if "''" in source:
            return False

        # We essentially want to count the number of quotes in the source, and make sure they are even.
        # Same with japanese quotes including the japanese style opening and closing quotes

        english_quote_count = source.count("'") + source.count('"')
        japanese_quote_count = target.count("＇") + target.count('＂')
        japanese_special_quotes = target.count("「") + target.count("」") + target.count("『") + target.count("』")
        if english_quote_count % 2 != 0 or japanese_quote_count % 2 != 0 or japanese_special_quotes % 2 != 0:
            return False

        return True

    def clean(self, source, target):
        """
        Remove unbalanced quotes from the data.
        """


        # Remove double quotes from the data
        source = source.replace('""', '"')
        target = target.replace('""', '"')

        return (source, target)