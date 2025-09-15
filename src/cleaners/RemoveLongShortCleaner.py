from .BaseCleaner import BaseCleaner

class RemoveLongShortCleaner(BaseCleaner):
    MAX_LENGTH = 100
    MIN_LENGTH = 3

    def clean(self, source, target):
        """
        Remove long and short data from the data.
        """
        pass