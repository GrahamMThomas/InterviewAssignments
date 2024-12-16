from dataclasses import dataclass, field

@dataclass
class Barcode:
    # Looks like order_id and barcode are auto incrementing int ID numbers,
    # We won't need any numerical operations so let's use strings.
    # We may hit the max size supported by int with enough scale, 
    # so using string will allow us to move to GUIDs if needed.

    barcode: str
    order_id: str = None

    def __post_init__(self):
        if not self.barcode.strip():
            raise ValueError("barcode is required")
        # Barcode can be empty if it hasn't been sold
        
        # TODO: Maybe limit to digits only