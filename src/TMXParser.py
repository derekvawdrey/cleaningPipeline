import lxml.etree as etree
import PythonTmx as tmx

class TMXParser:

    loadedPairs = []

    def __init__(self):
        pass

    def load_tmx_file(self, file_path):
        tmx_file: etree._ElementTree = etree.parse(
            file_path, etree.XMLParser(encoding="utf-8")
        )
        tmx_root: etree._Element = tmx_file.getroot()
        tmx_obj: tmx.TmxElement = tmx.from_element(tmx_root)
        assert isinstance(tmx_obj, tmx.Tmx), "The TMX file is not valid"