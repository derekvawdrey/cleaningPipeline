from .BasePostCleaner import BasePostCleaner

class LengthRatioCleaner(BasePostCleaner):
    def clean(self, source_data, target_data):
        """
        Clean the data.
        """
        return (source_data, target_data)