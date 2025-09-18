from .BaseCleaner import BaseCleaner
import re
class WhiteSpaceRatioCleaner(BaseCleaner):
    def validate(self, source, target):
        """
        Validate the data. If the ratio of whitespace to non-whitespace is greater than 0.30, return false
        Average whitespace ratio is 0.167, so we want to make sure it is less than 0.30
        """
        whitespace_count = len(re.findall(r'\s', source))
        non_whitespace_count = len(re.findall(r'\S', source))
        if non_whitespace_count == 0:
            return False
        if whitespace_count / non_whitespace_count > 0.30:
            return False
            
        whitespace_count = len(re.findall(r'\s', target))
        if whitespace_count / non_whitespace_count > 0.30:
            return False
        return True

    def clean(self, source, target):
        """
        Clean the data.
        """
        target = " ".join(target.split()).strip()
        source = " ".join(source.split()).strip()
        return (source, target)