from .BaseCleaner import BaseCleaner

class RemoveSenselessCleaner(BaseCleaner):
    def clean(self, source, target):
        """
        Remove senseless data from the data.
        Essentially, this is data that is almost purely punctuation, whitespace, or tags
        """
        pass