from dataclasses import dataclass, field


@dataclass
class Order:
    order_id: int
    customer_id: int

    def __post_init__(self):
        if not self.order_id.strip():
            raise ValueError("order_id is required")

        self.order_id = int(self.order_id)

        if not self.customer_id.strip():
            raise ValueError("customer_id is required")

        self.customer_id = int(self.customer_id)
