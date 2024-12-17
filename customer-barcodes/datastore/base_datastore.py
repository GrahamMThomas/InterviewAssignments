from abc import ABC, abstractmethod
from typing import List


class BaseDataStore(ABC):
    def save(self, obj) -> None:
        pass

    def get_customer_report(self, file_path: str) -> None:
        pass

    def get_unsold_barcodes(self) -> List[str]:
        pass

    def get_top_customers(self, n: int) -> dict:
        pass
