from .BaseCleaner import BaseCleaner
import regex

class RemoveSenselessCleaner(BaseCleaner):

    def validate(self, source, target):
        """
        Validate the data.
        """
        japanese_pattern = regex.compile(r'[\p{IsHiragana}\p{IsKatakana}\p{IsHan}]', regex.UNICODE)
        if not japanese_pattern.search(target):
            return False


        # If it is blank, return false
        if(source.strip() == "" or target.strip() == ""):
            return False

        # If all the text is between <> return false
        source_match = regex.match(r'<.*>', source)
        target_match = regex.match(r'<.*>', target)
        if source_match or target_match:
            return False
            
        return True

    def clean(self, source, target):
        """
        Remove senseless data from the data.
        Essentially, this is data that is almost purely punctuation, whitespace, or tags
        """

        # Remove unnecessary characters like …, \\, //
        source = source.replace("…", "")
        source = source.replace("\\\\", "")
        target = target.replace("\\\\", "")

        return (source, target)