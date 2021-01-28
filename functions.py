import csv
from datetime import datetime


def current_rent():
    with open('python_developer_test_dataset.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        sorted_rows = sorted(
            csv_reader,
            key=lambda row: float(row['Current Rent']),
            reverse=False
        )

    return sorted_rows[0:5]


def lease_years():
    with open('python_developer_test_dataset.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        rows = [row for row in csv_reader if row['Lease Years'] == '25']

    return rows


def total_rent():
    rows = lease_years()
    rent = [float(row['Current Rent']) for row in rows]
    result = sum(rent)

    return result


def masts_per_tenant():
    with open('python_developer_test_dataset.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        tenants = dict()
        for row in csv_reader:
            if row['Tenant Name'] in tenants:
                tenants[row['Tenant Name']] += 1
            else:
                tenants[row['Tenant Name']] = 1

    return tenants


def lease_start_date():
    start_date = datetime.strptime('1 Jun 1999', '%d %b %Y')
    end_date = datetime.strptime('31 Aug 2007', '%d %b %Y')

    with open('python_developer_test_dataset.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        rows = list()
        for row in csv_reader:
            lease_start = datetime.strptime(row['Lease Start Date'], '%d %b %Y')
            lease_end = datetime.strptime(row['Lease End Date'], '%d %b %Y')
            if lease_start >= start_date and lease_start <= end_date:
                row['Lease Start Date'] = datetime.datetime.strftime(
                    lease_start, '%d/%m/%Y'
                )
                row['Lease End Date'] = datetime.datetime.strftime(
                    lease_end, '%d/%m/%Y'
                )
                rows.append(row)

    return rows

