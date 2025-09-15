from .BaseCleaner import BaseCleaner

class EmptySegmentCleaner(BaseCleaner):

    def validate(self, source, target):
        """
        Validate the data.
        """
        return True

    def clean(self, source, target):
        """
        Remove empty segments from the data (Things that are not a segment, but are in the data).
        """
        return [
            {
                "source": source,
                "target": target,
            }
        ]