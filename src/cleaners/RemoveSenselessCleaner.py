from .BaseCleaner import BaseCleaner

class RemoveSenselessCleaner(BaseCleaner):

    def validate(self, source, target):
        """
        Validate the data.
        """
        if(source.strip() == "" or target.strip() == ""):
            return False
        return True


    def clean(self, source, target):
        """
        Remove senseless data from the data.
        Essentially, this is data that is almost purely punctuation, whitespace, or tags
        """
        pass