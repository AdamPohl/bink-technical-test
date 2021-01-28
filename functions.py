import csv
from datetime import datetime
from pprint import pprint


class PhoneMasts():
    def make_csv_reader(self):
        self.csv_file = open('python_developer_test_dataset.csv', 'r')
        csv_reader = csv.DictReader(self.csv_file, delimiter=',')

        return csv_reader

    def current_rent(self):
        """
        This function deals with requirement 1 of the test.

        :return: The first 5 items of the list sorted in ascending order by
                `Current Rent` are pretty printed to the console.
        """
        csv_reader = self.make_csv_reader()
        sorted_rows = sorted(
            csv_reader, key=lambda row: float(row['Current Rent']), reverse=False
        )
        self.csv_file.close()

        pprint(sorted_rows[0:5])
        return sorted_rows[0:5]

    def lease_years(self):
        """
        This function deals with requirement 2.a of the test.

        :return: 
        """
        csv_reader = self.make_csv_reader()
        rows = [row for row in csv_reader if row['Lease Years'] == '25']
        self.csv_file.close()

        pprint(rows)
        return rows

    def total_rent(self):
        """
        This function deals with requirement 2.b of the test.

        :return: 
        """
        rows = self.lease_years()
        rent = [float(row['Current Rent']) for row in rows]
        self.csv_file.close()
        result = sum(rent)

        pprint(result)
        return result

    def masts_per_tenant(self):
        """
        This function deals with requirement 3 of the test.

        :return: 
        """
        csv_reader = self.make_csv_reader()
        tenants = dict()
        for row in csv_reader:
            if row['Tenant Name'] in tenants:
                tenants[row['Tenant Name']] += 1
            else:
                tenants[row['Tenant Name']] = 1
        self.csv_file.close()

        pprint(tenants)
        return tenants

    def lease_start_date(self):
        """
        This function deals with requirement 4 of the test.

        :return: 
        """
        start_date = datetime.strptime('1 Jun 1999', '%d %b %Y')
        end_date = datetime.strptime('31 Aug 2007', '%d %b %Y')

        csv_reader = self.make_csv_reader()
        rows = list()
        for row in csv_reader:
            lease_start = datetime.strptime(row['Lease Start Date'], '%d %b %Y')
            lease_end = datetime.strptime(row['Lease End Date'], '%d %b %Y')
            if lease_start >= start_date and lease_start <= end_date:
                row['Lease Start Date'] = datetime.strftime(
                    lease_start, '%d/%m/%Y'
                )
                row['Lease End Date'] = datetime.strftime(lease_end, '%d/%m/%Y')
                rows.append(row)
        self.csv_file.close()

        pprint(rows)
        return rows

    def all(self):
        self.current_rent()
        print('\n')
        self.lease_years()
        print('\n')
        self.total_rent()
        print('\n')
        self.masts_per_tenant()
        print('\n')
        self.lease_start_date()


if __name__ == '__main__':
    option = input('Hi there, what requirement would you like to see? ')
    phone_masts = PhoneMasts()

    while option != "exit":
        if option == "Current rent":
            phone_masts.current_rent()
        elif option == "Lease years":
            phone_masts.lease_years()
        elif option == "Total rent":
            phone_masts.total_rent()
        elif option == "Masts per tenant":
            phone_masts.masts_per_tenant()
        elif option == "Lease start date":
            phone_masts.lease_start_date()
        elif option == "All":
            phone_masts.all()

        option = input(
            '\nGreat, is there another requirement you would like to see? '
        )
