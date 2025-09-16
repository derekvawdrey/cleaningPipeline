from .BaseCleaner import BaseCleaner
import re

class NonTextCleaner(BaseCleaner):

    def validate(self, source, target):
        """
        Validate the data.
        """
        # Count the number of non-text characters in the source
        # If the ratio is above 85% return false
        non_text_count = len(re.findall(r'[^a-zA-Z\s]', source))
        if non_text_count > 0.85 * len(source):
            return False
        
        
            
        return True

    def clean(self, source, target):
        """
        Remove non-text data from the data.
        """
        return (source, target)