from abc import ABC, abstractmethod
from typing import List


class BaseDataProvider:
    @abstractmethod
    def get_data(self) -> List[dict]:
        pass
