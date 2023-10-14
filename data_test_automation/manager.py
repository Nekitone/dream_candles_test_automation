from utils import read_customer_sample, read_csv_chunks, store_data
from data_models import customer_adapter, invoice_adapter, invoice_item_adapter


class WorkManager:

    def __init__(self, customer_sample_file: str, customer_file: str, invoice_file: str, invoice_item_file: str) -> None:
        self._customer_sample_file = customer_sample_file
        self._customer_file = customer_file
        self._invoice_file = invoice_file
        self._invoice_item_file = invoice_item_file

    def run(self) -> None:
        # open customer sample file return a list of customer codes
        customer_ids = read_customer_sample(self._customer_sample_file)

        customers_list = []
        # open customer file and return a list of objects with the customer codes in the customer list
        for batch in read_csv_chunks(self._customer_file, customer_adapter):
            customers = [customer for customer in batch if customer.CUSTOMER_CODE in customer_ids]
            customers_list.extend(customers)
        store_data(customers_list, self._customer_file)

        # open invoice file and return a list of objects with the customer codes in the customer list
        invoices_list = []
        for batch in read_csv_chunks(self._invoice_file, invoice_adapter):
            invoices = [invoice for invoice in batch if invoice.CUSTOMER_CODE in customer_ids]
            invoices_list.extend(invoices)
        store_data(invoices_list, self._invoice_file)

        # open invoice file and return a list of objects with the customer codes in the customer list
        invoices_items_list = []
        for batch in read_csv_chunks(self._invoice_item_file, invoice_item_adapter):
            invoices_items_list.extend(
                [it for it in batch if it.INVOICE_CODE in [invoice.INVOICE_CODE for invoice in invoices_list]]
            )
        store_data(invoices_items_list, self._invoice_item_file)
