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


        japanese_quote_map = {
            "‘": "＇",
            "’": "＇",
            "“": "＂",
            "”": "＂",
        }

        # Check if the source contains double or single quotes
        if any(quote in source for quote in english_quote_map):
            for quote in english_quote_map:
                source = source.replace(quote, english_quote_map[quote])
        if any(quote in target for quote in japanese_quote_map):
            for quote in japanese_quote_map:
                target = target.replace(quote, japanese_quote_map[quote])

        return (source, target)