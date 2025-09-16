from .BaseCleaner import BaseCleaner
import re

class NormalizeControlCharactersCleaner(BaseCleaner):
    def clean(self, source, target):
        """
        Normalize control characters in the data.
        """

        # Remove control characters from the data
        source = re.sub(r'[\u0000-\u001F\u007F-\u009F]', '', source)
        target = re.sub(r'[\u0000-\u001F\u007F-\u009F]', '', target)
        source = re.sub('\u2028', '', source)
        target = re.sub('\u2028', '', target)
        source = re.sub('\u2029', '', source)
        target = re.sub('\u2029', '', target)

        return (source, target)