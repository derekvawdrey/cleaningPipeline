from .BaseCleaner import BaseCleaner
import re

class UnbalancedQuoteCleaner(BaseCleaner):

    def validate(self, source, target):
        """
        Validate the data for balanced quotes.
        """
        # Check for double single quotes in source (often indicates formatting issues)
        if "''" in source:
            return False

        # Check English quotes balance
        english_double_count = source.count('"')

        # Check Japanese quotes balance (using new quote system)
        japanese_primary_open = target.count("「")
        japanese_primary_close = target.count("」")
        japanese_secondary_open = target.count("『")
        japanese_secondary_close = target.count("』")
        
        
        # Validate quote balance
        english_balanced = (english_double_count % 2 == 0)
        japanese_primary_balanced = japanese_primary_open == japanese_primary_close
        japanese_secondary_balanced = japanese_secondary_open == japanese_secondary_close
        
        return english_balanced and japanese_primary_balanced and japanese_secondary_balanced

    def clean(self, source, target):
        """
        Clean unbalanced quotes from the data.
        """
        # Remove double quotes from English text
        source = source.replace('""', '"')
        source = source.replace("''", "'")
        
        # Remove double quotes from Japanese text
        target = target.replace('""', '"')
        target = target.replace("''", "'")
        
        # Remove double Japanese quotes
        target = target.replace("「「", "「")
        target = target.replace("」」", "」")
        target = target.replace("『『", "『")
        target = target.replace("』』", "』")
        
        return (source, target)