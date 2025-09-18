from .BaseCleaner import BaseCleaner

class RemoveLongShortCleaner(BaseCleaner):
    MAX_LENGTH = 500
    MIN_LENGTH = 15
    JAPANESE_MAX_LENGTH = 300
    JAPANESE_MIN_LENGTH = 3

    def validate(self, source, target):
        """
        Validate the data.
        """
        if(len(source) > self.MAX_LENGTH or len(source) < self.MIN_LENGTH):
            return False
        # If more than 100 words in the source, return false
        split_source = source.split()
        if(len(split_source) > 95 or len(split_source) < 3):
            return False
        if(len(target) > self.JAPANESE_MAX_LENGTH or len(target) < self.JAPANESE_MIN_LENGTH):
            return False
        return True

    def clean(self, source, target):
        """
        Remove long and short data from the data.
        """
        return (source, target)