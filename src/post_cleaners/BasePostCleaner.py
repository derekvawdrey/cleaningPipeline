class BasePostCleaner:
    """
    Base class for post cleaners. 
    Post cleaners are used to clean data that requires the full dataset (i.e. duplicate cleaning)
    """
    def __init__(self):
        pass

    def clean(self, data: pd.DataFrame):
        pass