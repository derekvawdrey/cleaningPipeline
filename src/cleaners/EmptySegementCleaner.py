from .BaseCleaner import BaseCleaner

class EmptySegmentCleaner(BaseCleaner):
    def clean(self, original, target):
        """
        Remove empty segments from the data.
        """
        pass