from dataclasses import dataclass, field

@dataclass
class Order:
    order_id: str
    customer_id: str

    def __post_init__(self):
        if not self.order_id.strip():
            raise ValueError("order_id is required")
        
        if not self.customer_id.strip():
            raise ValueError("customer_id is required")