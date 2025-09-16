from .BaseCleaner import BaseCleaner
import re

class HtmlCleaner(BaseCleaner):
    def clean(self, source, target):
        """
        Clean the data.
        """
        source = re.sub(r"<[^>]+>", "", source)
        target = re.sub(r"<[^>]+>", "", target)
        return (source, target)