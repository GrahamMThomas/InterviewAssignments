import csv
from typing import List
from ingestion.parsers.base_parser import BaseParser


class CSVParser(BaseParser):
    def parse(self, file_path: str) -> List[dict]:
        with open(file_path, mode="r") as f:
            reader = csv.DictReader(f)
            return list(reader)
