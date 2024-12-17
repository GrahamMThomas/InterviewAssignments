from ingestion.parsers.base_parser import BaseParser
from ingestion.parsers.csv_parser import CSVParser


class ParserFactory:
    def create(self, file_path: str) -> BaseParser:
        if file_path.endswith(".csv"):
            return CSVParser()
        else:
            raise ValueError(f'Unsupported file format: {file_path.split(".")[-1]}')
