from .BaseCleaner import BaseCleaner
import html
import unicodedata
import re

class NormalizeEscapedCharactersCleaner(BaseCleaner):
    def clean(self, source, target):
        """
        Normalize escaped characters in the data.
        """

        # ： should be :
        source = source.replace("：", ":")
        target = target.replace("：", ":")

        source = source.replace("–", "-")
        target = target.replace("–", "-")

        # Handle multiple levels of HTML entity encoding (e.g., &amp;amp;nbsp;)
        while '&' in source and ';' in source:
            new_source = html.unescape(source)
            if new_source == source: 
                break
            source = new_source
            
        while '&' in target and ';' in target:
            new_target = html.unescape(target)
            if new_target == target:
                break
            target = new_target
        
        # Replace any &#\d
        source = re.sub(r'&#(\d+)', '', source)
        target = re.sub(r'&#(\d+)', '', target)

        source = unicodedata.normalize("NFKC", source)
        target = unicodedata.normalize("NFKC", target)

        source = source.replace("\\", "")
        target = target.replace("\\", "")

        # normalize whitespace
        source = " ".join(source.split())
        target = " ".join(target.split())

        return (source, target)
