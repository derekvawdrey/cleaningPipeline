from .BaseCleaner import BaseCleaner

class UnbalancedBracketCleaner(BaseCleaner):
    def clean(self, source, target):
        """
        Remove unbalanced brackets and quotes from the data using a stack.
        """
        pass