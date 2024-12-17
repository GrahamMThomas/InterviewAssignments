from typing import List
from ingestion.data_providers.base_data_provider import BaseDataProvider
from ingestion.parsers.parser_factory import ParserFactory


class FileDataProvider(BaseDataProvider):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def get_data(self) -> List[dict]:
        parser_factory = ParserFactory()
        parser = parser_factory.create(self.file_path)
        objs = parser.parse(self.file_path)

        return objs
