from .BaseCleaner import BaseCleaner

class RemoveLongShortCleaner(BaseCleaner):
    MAX_LENGTH = 500
    MIN_LENGTH = 15

    def validate(self, source, target):
        """
        Validate the data.
        """
        if(len(source) > self.MAX_LENGTH or len(source) < self.MIN_LENGTH):
            return False
        return True

    def clean(self, source, target):
        """
        Remove long and short data from the data.
        """
        return (source, target)