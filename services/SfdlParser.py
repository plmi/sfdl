#!/usr/bin/env python3

from typing import List
from models.Upload import Upload
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element


class SfdlParser:
    def __get(self, root: Element, name: str) -> str:
        return root.find(f'.//{name}').text

    def __get_bool(self, root: Element, name: str) -> bool:
        return self.__get(root, name) == 'true'

    def __get_any(self, root: Element, keywords: List[str]) -> str:
        for keyword in keywords:
            try:
                return self.__get(root, keyword)
            except Exception:
                pass

    def parse(self, xml_path: str) -> Upload:
        root: Element = ET.parse(xml_path).getroot()
        return Upload(
            self.__get(root, 'Host'),
            self.__get(root, 'Username'),
            self.__get(root, 'Password'),
            self.__get(root, 'Port'),
            self.__get(root, 'Description'),
            self.__get(root, 'Uploader'),
            self.__get_any(root, ['DefaultPath', 'Path']),
            self.__get(root, 'BulkFolderPath'),
            self.__get(root, 'PackageName'),
            self.__get_bool(root, 'Encrypted')
        )
