import click

from manager import WorkManager


@click.command()
@click.argument('customer-sample-file', type=click.STRING)
@click.argument('customer-file', type=click.STRING)
@click.argument('invoice-file', type=click.STRING)
@click.argument('invoice-item-file', type=click.STRING)
def create_integration_test_files(
        customer_sample_file: str,
        customer_file: str,
        invoice_file: str,
        invoice_item_file: str
):

    manager = WorkManager(customer_sample_file, customer_file, invoice_file, invoice_item_file)
    manager.run()


if __name__ == '__main__':
    create_integration_test_files()
