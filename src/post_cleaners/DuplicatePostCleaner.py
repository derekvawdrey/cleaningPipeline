from .BasePostCleaner import BasePostCleaner

class DuplicatePostCleaner(BasePostCleaner):
    def clean(self, source_data, target_data):
        """
        Remove duplicates from source and target data while maintaining alignment.
        If a source-target pair is duplicated, only keep the first occurrence.
        
        Args:
            source_data: List of source text segments
            target_data: List of target text segments
            
        Returns:
            Tuple of (cleaned_source_data, cleaned_target_data) with duplicates removed
        """
        if len(source_data) != len(target_data):
            raise ValueError("Source and target data must have the same length")
        
        seen_target = set()
        seen_source = set()
        cleaned_source = []
        cleaned_target = []
        
        for i, (source, target) in enumerate(zip(source_data, target_data)):

            # Only add if we haven't seen this exact pair before
            if target.lower() not in seen_target and source.lower() not in seen_source:
                seen_target.add(target.lower())
                seen_source.add(source.lower())
                cleaned_source.append(source)
                cleaned_target.append(target)
        
        return cleaned_source, cleaned_target