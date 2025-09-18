from .BasePostCleaner import BasePostCleaner

class LengthRatioCleaner(BasePostCleaner):

    def clean(self, source_data, target_data):
        """
        Remove data where the source is 30% longer than the target.
        """
        if len(source_data) != len(target_data):
            raise ValueError("Source and target data must have the same length")

        cleaned_source = []
        cleaned_target = []
        threshold = 2.5

        for src, tgt in zip(source_data, target_data):
            src_len = len(src)
            tgt_len = len(tgt)
            if src_len == 0 or tgt_len == 0:
                continue
            ratio = max(src_len, tgt_len) / min(src_len, tgt_len)
            if ratio <= threshold:
                cleaned_source.append(src)
                cleaned_target.append(tgt)


        return cleaned_source, cleaned_target