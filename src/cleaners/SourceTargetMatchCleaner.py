from .BaseCleaner import BaseCleaner

class SourceTargetMatchCleaner(BaseCleaner):
    def validate(self, source, target):
        """
        Validate the data.
        """
        if(source == target):
            return False
        return True


    def clean(self, source, target):
        """
        Clean the data.
        """
        return (source, target)