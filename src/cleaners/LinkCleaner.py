from .BaseCleaner import BaseCleaner

class LinkCleaner(BaseCleaner):
    def clean(self, source, target):
        """
        Clean the data.
        """

        # Remove links from the data
        source = re.sub(r'https?://\S+', '', source)
        target = re.sub(r'https?://\S+', '', target)

        return (source, target)