from .BaseCleaner import BaseCleaner

class ContainsNoSpacesCleaner(BaseCleaner):
    """
    Cleaner that removes data that contains no spaces.
    """
    def validate(self, source, target):
        """
        Validate the data.
        """
        if " " in source or " " in target:
            return True
        return False

    def clean(self, source, target):
        """
        Clean the data.
        """
        return (source, target)