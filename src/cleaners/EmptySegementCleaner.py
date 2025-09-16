from .BaseCleaner import BaseCleaner

class EmptySegmentCleaner(BaseCleaner):

    def validate(self, source, target):
        """
        Validate the data.
        """
        if(source.strip() == "" or target.strip() == ""):
            return False
        return True

    def clean(self, source, target):
        """
        Remove empty segments from the data (Things that are not a segment, but are in the data).
        And also strip the data of any trailing or leading whitespace.
        """
        return (source.strip(), target.strip())