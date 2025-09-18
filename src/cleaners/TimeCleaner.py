from .BaseCleaner import BaseCleaner
import re

class TimeCleaner(BaseCleaner):

    def validate(self, source, target):
        """
        Validate the data.

        If the string contains more than 2 a.m or p.m and their combined count is more than 3, return false
        """
        a_m_count = len(re.findall(r'a\.m\.', source))
        p_m_count = len(re.findall(r'p\.m\.', source))
        if a_m_count + p_m_count > 3:
            return False

        return True

    def clean(self, source, target):
        """
        Clean the data.
        """
        return (source, target)