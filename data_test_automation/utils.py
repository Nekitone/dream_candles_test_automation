import os
import csv
import json
from data_models import Customer

def read_customer_sample(file_name):
    customer_sample = []
    with open(file_name) as csvfile:
        data_reader = csv.reader(csvfile)
        headers = next(data_reader, None)[1:-1]

        for row in data_reader:
            customer_sample.append(row[0][1:-1])

    return customer_sample


def read_csv_chunks(filename: str, data_adapter, batch_limit: int = 1) -> list:

    data_list = []
    with open(filename) as csvfile:
        data_reader = csv.DictReader(csvfile)

        for row in data_reader:
            row = {k[1:-1]: v[1:-1] for (k, v) in row.items()}

            data_list.append(
                data_adapter(row)
            )

            if len(data_list) == batch_limit:
                yield data_list
                data_list = []

        if data_list:
            yield data_list


def create_files_path_for_testing(file_path: str) -> str:
    f_splited = os.path.split(file_path)
    return os.path.join(f_splited[0], f'test_{f_splited[1]}')


def store_data(data_list: list, filename: str) -> None:
    new_filename = create_files_path_for_testing(filename)

    with open(new_filename, "w") as nf:
        writer = csv.DictWriter(nf, fieldnames=data_list[0].dict().keys())
        writer.writeheader()
        for data in data_list:
            writer.writerow(data.dict())
