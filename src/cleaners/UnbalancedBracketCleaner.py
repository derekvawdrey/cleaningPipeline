from .BaseCleaner import BaseCleaner

class UnbalancedBracketCleaner(BaseCleaner):

    def validate(self, source, target):
        bracket_stack = []
        opening_brackets = ["(", "[", "{", "<"]
        closing_brackets = [")", "]", "}", ">"]
        for char in source:
            if char in opening_brackets:
                bracket_stack.append(char)
            elif char in closing_brackets:
                if not bracket_stack:
                    return False
                if bracket_stack[-1] == opening_brackets[closing_brackets.index(char)]:
                    bracket_stack.pop()
        
        
        japanese_bracket_stack = []
        for char in target:
            if char in opening_brackets:
                japanese_bracket_stack.append(char)
            elif char in closing_brackets:
                if not japanese_bracket_stack:
                    return False
                if japanese_bracket_stack[-1] == opening_brackets[closing_brackets.index(char)]:
                    japanese_bracket_stack.pop()
        
        return len(bracket_stack) == 0 and len(japanese_bracket_stack) == 0


    def clean(self, source, target):
        """
        Remove unbalanced brackets and quotes from the data using a stack.
        """
        return (source, target)