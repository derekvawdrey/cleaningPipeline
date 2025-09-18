import re
from .BaseCleaner import BaseCleaner


class NormalizeQuoteCleaner(BaseCleaner):
    def clean(self, source, target):
        """
        Normalize quotes in the data with improved handling for English and Japanese quotes.
        """
        # Clean English quotes in source
        source = self.normalize_english_quotes(source)
        
        # Clean Japanese quotes in target
        target = self.normalize_english_quotes(target)
        target = self.normalize_japanese_quotes(target)
        
        return (source, target)
    

    def normalize_japanese_quotes(self, text):
        """
        Replace English single and double quotes in the input text with Japanese quotation marks.
        Double quotes → 「」
        Single quotes within double quotes (nested) → 『』
        Assumes properly paired quotes.
        Avoids replacing single quotes that are between letters (like in contractions).
        """
        result = []
        double_quote_stack = []
        single_quote_stack = []
        
        for i, char in enumerate(text):
            if char == '"':
                if not double_quote_stack:
                    result.append('「')
                    double_quote_stack.append('"')
                else:
                    result.append('」')
                    double_quote_stack.pop()
            elif char == "'":
                # Check if this single quote is between letters (like in contractions)
                is_between_letters = (
                    i > 0 and i < len(text) - 1 and
                    text[i-1].isalnum() and text[i+1].isalnum()
                )

                # Also check if this single quote is for a name or not
                is_name = (
                    i > 0 and i < len(text) - 1 and
                    text[i-1] not in [".", ",", "!", "?", ":", ";"] and text[i+1] == " "
                )

                if is_between_letters or is_name:
                    # Preserve apostrophes between letters
                    result.append(char)
                elif double_quote_stack:
                    if not single_quote_stack:
                        result.append('『')
                        single_quote_stack.append("'")
                    else:
                        result.append('』')
                        single_quote_stack.pop()
                else:
                    result.append(char)
            else:
                result.append(char)
        
        return ''.join(result)


    def normalize_english_quotes(self, text):
        """
        Normalize English quotes and handle apostrophe-like patterns.
        """
        # Map various quote types to standard quotes
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
        
        # Apply quote mapping
        for old_quote, new_quote in english_quote_map.items():
            if old_quote != new_quote:  # Skip identity mappings
                text = text.replace(old_quote, new_quote)
        
        return text
    