from .BaseCleaner import BaseCleaner
import html

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

        # Remove LS and other

        source = html.unescape(source)
        target = html.unescape(target)

        source = source.replace("\\", "")
        target = target.replace("\\", "")

        return (source, target)
