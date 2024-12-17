from abc import ABC, abstractmethod
from typing import List


class BaseParser(ABC):
    @abstractmethod
    def parse(self, file_path: str) -> List[dict]:
        pass
