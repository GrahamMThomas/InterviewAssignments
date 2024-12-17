import sys
from typing import List
from datastore.base_datastore import BaseDataStore
from models.barcode import Barcode
from models.order import Order
import pandas as pd


class MemoryDataStore(BaseDataStore):
    """Creates a memory data store. Functionality this is a mock sql data base."""

    orders: pd.DataFrame
    barcodes: pd.DataFrame

    def __init__(self):
        self.orders = pd.DataFrame()
        self.barcodes = pd.DataFrame()

    def save(self, obj) -> None:
        """Saves supported objects to data store.

        Args:
            obj (Order | Barcode): Object to save

        Raises:
            TypeError: If type is not supported
        """
        # Optimally, these checks should be implemented via constraints in a relational database.

        if isinstance(obj, Order):
            if len(self.barcodes[self.barcodes["order_id"] == obj.order_id]) == 0:
                print(
                    f"Attempted to save an order but barcode does not exist. Skipping: Order ID: {obj.order_id}",
                    file=sys.stderr,
                )
                return
            self.orders = pd.concat([self.orders, pd.DataFrame([obj.__dict__]).set_index("order_id")])

        elif isinstance(obj, Barcode):
            if obj.barcode in self.barcodes.index:
                print(f"Duplicate Barcode detected: {obj.barcode}. Skipping.", file=sys.stderr)
                return
            self.barcodes = pd.concat([self.barcodes, pd.DataFrame([obj.__dict__]).set_index("barcode")])
        else:
            raise TypeError(f"Object type not supported: {obj.__class__.__name__}")

    def get_customer_report(self, file_path: str) -> None:
        """Create customer report and output it to the file_path specified.

        Args:
            file_path (str): file_path to output report to.
        """

        merged = pd.merge(
            self.orders.reset_index(), self.barcodes.reset_index(), left_on="order_id", right_on="order_id"
        )
        customer_report = merged.groupby(["customer_id", "order_id"]).aggregate(
            {"customer_id": "first", "order_id": "first", "barcode": list}
        )
        customer_report.to_csv(file_path, index=False)

    def get_unsold_barcodes(self) -> List[str]:
        """Get unsold barcodes.

        Returns:
            List[str]: List of unsold barcodes.
        """

        unsold_barcodes = self.barcodes[self.barcodes["order_id"].isnull()]
        return unsold_barcodes.index.tolist()

    def get_top_customers(self, n: int) -> dict:
        """Get top n customers.

        Args:
            n (int): Number of top customers to get.

        Returns:
            dict: contains dict where key are customerId and value is ticket count.
        """
        merged = pd.merge(
            self.orders.reset_index(), self.barcodes.reset_index(), left_on="order_id", right_on="order_id"
        )
        top_customers = (
            merged.groupby("customer_id")
            .aggregate({"order_id": "count"})
            .sort_values(by="order_id", ascending=False)
            .take(range(n))
        )
        return top_customers.to_dict()["order_id"]
