import lxml.etree as etree
import PythonTmx as tmx

class TMXParser:

    def __init__(self):
        self.loadedPairs = []

    def load_tmx_file(self, file_path):
        tmx_file: etree._ElementTree = etree.parse(
            file_path, etree.XMLParser(encoding="utf-8")
        )
        tmx_root: etree._Element = tmx_file.getroot()
        tmx_obj: tmx.TmxElement = tmx.from_element(tmx_root)

        # Remove incomplete translation units (keep only those with 2 or more variants)
        tmx_obj.tus = [tu for tu in tmx_obj.tus if len(tu.tuvs) >= 2]
                
        assert isinstance(tmx_obj, tmx.Tmx), "The TMX file is not valid"

        pairs = []
        for tu in tmx_obj.tus:
            # Find English and Japanese variants
            english_text = None
            japanese_text = None
            
            for tuv in tu.tuvs:
                if(tuv.lang == "en-US") and (len(tuv.content) == 1):
                    english_text = tuv.content[0]
                elif(tuv.lang == "ja-JP") and (len(tuv.content) == 1):
                    japanese_text = tuv.content[0]

            # Only add pairs where we have both English and Japanese
            if english_text is not None and japanese_text is not None:
                pairs.append({
                    'source': english_text,
                    'target': japanese_text
                })

        self.loadedPairs.extend(pairs)

        return pairs