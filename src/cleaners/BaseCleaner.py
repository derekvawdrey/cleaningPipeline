class BaseCleaner():
    def __init__(self):
        pass

    def validate(self, source, target):
        """
        Validate the data before cleaning. This will be used to determine if the data should be added or not.
        """
        return True

    def clean(self, source, target):
        """
        Clean the data. This will be used to clean the data and return the cleaned data.
        """
        pass