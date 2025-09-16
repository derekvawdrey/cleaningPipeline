from .BaseCleaner import BaseCleaner

class NormalizeQuoteCleaner(BaseCleaner):
    def clean(self, source, target):
        """
        Normalize quotes in the data.
        """

        english_quote_map = {
            # Straight/neutral quotes
            "'": "'",
            '"': '"',

            # Curly/smart single quotes
            "’": "'",
            "‘": "'",
            "‛": "'",   # SINGLE HIGH-REVERSED-9 QUOTATION MARK
            "‚": "'",   # SINGLE LOW-9 QUOTATION MARK

            # Curly/smart double quotes
            "“": '"',
            "”": '"',
            "„": '"',   # DOUBLE LOW-9 QUOTATION MARK
            "‟": '"',   # DOUBLE HIGH-REVERSED-9 QUOTATION MARK

            # Angle quotes (guillemets and single guillemets)
            "«": '"',   # LEFT DOUBLE ANGLE QUOTATION MARK
            "»": '"',   # RIGHT DOUBLE ANGLE QUOTATION MARK
            "‹": "'",   # LEFT SINGLE ANGLE QUOTATION MARK
            "›": "'",   # RIGHT SINGLE ANGLE QUOTATION MARK
        }


        japaneseQuoteMap = {
            "‘": "＇",
            "’": "＇",
            "“": "＂",
            "”": "＂",
        }

        # Check if the source contains double or single quotes
        if any(quote in source for quote in englishQuoteMap):
            for quote in englishQuoteMap:
                source = source.replace(quote, englishQuoteMap[quote])
        if any(quote in target for quote in japaneseQuoteMap):
            for quote in japaneseQuoteMap:
                target = target.replace(quote, japaneseQuoteMap[quote])

        return (source, target)