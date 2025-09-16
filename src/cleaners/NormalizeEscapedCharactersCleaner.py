from .BaseCleaner import BaseCleaner

class NormalizeEscapedCharactersCleaner(BaseCleaner):
    def clean(self, source, target):
        """
        Normalize escaped characters in the data.
        """

        # ： should be :
        source = source.replace("：", ":")
        target = target.replace("：", ":")

        return (source, target)
