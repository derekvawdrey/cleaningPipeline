from .BaseCleaner import BaseCleaner

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

        # TODO: Turn escaped characters into their actual characters

        source = source.replace("\\", "")
        target = target.replace("\\", "")

        return (source, target)
