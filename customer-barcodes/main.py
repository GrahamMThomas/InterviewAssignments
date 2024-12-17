import os
from datastore.memory_datastore import MemoryDataStore
from helpers.dict_utility import create_objects_from_dicts
from ingestion.data_providers.file_data_provider import FileDataProvider
from ingestion.parsers.parser_factory import ParserFactory
from models.barcode import Barcode
from models.order import Order

DATA_DIR = "data"
OUTPUT_DIR = "_output"


def main():
    # Load in Data
    barcode_location = os.path.join(DATA_DIR, "barcodes.csv")
    order_location = os.path.join(DATA_DIR, "orders.csv")

    barcode_objs = FileDataProvider(barcode_location).get_data()
    barcodes = create_objects_from_dicts(Barcode, barcode_objs)

    order_objs = FileDataProvider(order_location).get_data()
    orders = create_objects_from_dicts(Order, order_objs)

    # Save Data
    data_store = MemoryDataStore()

    for barcode in barcodes:
        data_store.save(barcode)

    for order in orders:
        data_store.save(order)

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Generate Reports
    report_path = os.path.join(OUTPUT_DIR, "customer_report.csv")
    data_store.get_customer_report(report_path)

    print()
    print("Top 5 Customers:")
    for k, v in data_store.get_top_customers(5).items():
        print(f"Customer ID: {k}, Number of Tickets: {v}")

    print()
    unsold_barcodes = data_store.get_unsold_barcodes()
    print(f"Unsold barcodes: {len(unsold_barcodes)}")

    print()
    print(f"📃 Report Output Location: {report_path}")


if __name__ == "__main__":
    main()
