from pydantic import BaseModel


class Customer(BaseModel):
    CUSTOMER_CODE: str
    FIRSTNAME: str
    LASTNAME: str

def customer_adapter(customer_dict: dict) -> Customer:
    return Customer(**customer_dict)


class Invoice(BaseModel):
    CUSTOMER_CODE: str
    INVOICE_CODE: str
    AMOUNT: str
    DATE: str

def invoice_adapter(invoice_dict: dict) -> Invoice:
    return Invoice(**invoice_dict)


class InvoiceItem(BaseModel):
    INVOICE_CODE: str
    ITEM_CODE: str
    AMOUNT: float
    QUANTITY: int

def invoice_item_adapter(invoice_item_dict: dict) -> InvoiceItem:
    return InvoiceItem(**invoice_item_dict)
