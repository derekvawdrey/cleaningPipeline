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
        
        # If text starts with a. or 1.
        source_match = regex.match(r'^[a-z|0-9]\.', source)
        target_match = regex.match(r'^[a-z|0-9]\.', target)
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
        target = target.replace("…", "")
        source = source.replace("\\\\", "")
        target = target.replace("\\\\", "")

        source = source.replace("\u3000", "")
        target = target.replace("\u3000", "")

        source = source.replace("\u30fb", "")
        target = target.replace("\u30fb", "")

        source = source.replace("\u2022", "")
        target = target.replace("\u2022", "")

        # Use this regex
        source = regex.sub(r'&[A-Za-z]-', '', source)
        target = regex.sub(r'&[A-Za-z]-', '', target)
        
        return (source, target)