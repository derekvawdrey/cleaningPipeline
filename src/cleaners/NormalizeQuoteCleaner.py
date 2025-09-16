from .BaseCleaner import BaseCleaner

class NormalizeQuoteCleaner(BaseCleaner):
    def clean(self, source, target):
        """
        Normalize quotes in the data.
        """

        englishQuotes = ["\"", "\'", "“", "”", "‘", "’", "«", "»"]
        japaneseQuotes = ["」", "「", "『", "』"]

        # Replace english quotes with japanese quotes
        if any(quote in source for quote in englishQuotes):
            for quote in englishQuotes:
                source = source.replace(quote, englishQuotes[0])
        if any(quote in target for quote in japaneseQuotes):
            for quote in japaneseQuotes:
                target = target.replace(quote, englishQuotes[0])

        # Check if the source contains double or single quotes

        return (source, target)