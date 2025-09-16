from .BaseCleaner import BaseCleaner
import regex

class VariableCleaner(BaseCleaner):
    def validate(self, source, target):
        """
        Validate the data.
        """
        # If there is a variable in the form of $.*
        if regex.match(r'\$(?!\d)', source):
            return False
        if regex.match(r'\$(?!\d)', target):
            return False

        # If there is a variable in the form of <.*>
        source_match = regex.match(r'<.*>', source)
        target_match = regex.match(r'<.*>', target)
        if source_match or target_match:
            return False

        # If there is a variable in the form of {{.*}}
        source_match = regex.match(r'{{.*}}', source)
        target_match = regex.match(r'{{.*}}', target)
        if source_match or target_match:
            return False

        return True

    def clean(self, source, target):
        """
        Clean the data.
        """
        return (source, target)