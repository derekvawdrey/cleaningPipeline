from .BaseCleaner import BaseCleaner
import re

class MostlyNumberCleaner(BaseCleaner):
    def validate(self, source, target):
        """
        Validate the data.
        If the string contains more than 20% numbers, return false
        """
        
        number_count = len(re.findall(r'\d', source))
        if number_count > 0.40 * len(source):
            return False
        
        number_count = len(re.findall(r'\d', target))
        if number_count > 0.40 * len(target):
            return False
        
        return True

    def clean(self, source, target):
        """
        Clean the data.
        """
        return (source, target)