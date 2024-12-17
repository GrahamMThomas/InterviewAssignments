from dataclasses import dataclass, field


@dataclass
class Barcode:
    barcode: int
    order_id: int = None  # empty if it hasn't been sold

    def __post_init__(self):
        if not self.barcode.strip():
            raise ValueError("barcode is required")

        self.barcode = int(self.barcode)
        self.order_id = int(self.order_id) if self.order_id else None
