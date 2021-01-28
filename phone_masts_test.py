from unittest import TestCase
from unittest.mock import Mock
from phone_masts import PhoneMasts

SUCCESS_TEST_DATA = [
    {
        "Tenant Name": "Tony Stark",
        "Lease Start Date": "02 May 2008",
        "Lease End Date": "25 Apr 2019",
        "Lease Years": "11",
        "Current Rent": "12400.02",
    },
    {
        "Tenant Name": "Tony Stark",
        "Lease Start Date": "01 Mar 1963",
        "Lease End Date": "25 May 1988",
        "Lease Years": "25",
        "Current Rent": "3900.00",
    },
    {
        "Tenant Name": "Tony Stank",
        "Lease Start Date": "26 Apr 2016",
        "Lease End Date": "25 Apr 2023",
        "Lease Years": "7",
        "Current Rent": "11530.64",
    },
    {
        "Tenant Name": "Steve Rodgers",
        "Lease Start Date": "02 May 1944",
        "Lease End Date": "25 Apr 2012",
        "Lease Years": "68",
        "Current Rent": "370.68",
    },
    {
        "Tenant Name": "Bruce Banner",
        "Lease Start Date": "13 Jun 2008",
        "Lease End Date": "25 Apr 2019",
        "Lease Years": "11",
        "Current Rent": "264.8",
    },
    {
        "Tenant Name": "Black Widow",
        "Lease Start Date": "30 Apr 2010",
        "Lease End Date": "7 May 2021",
        "Lease Years": "11",
        "Current Rent": "200150.90",
    },
    {
        "Tenant Name": "Point Break",
        "Lease Start Date": "27 Apr 2011",
        "Lease End Date": "25 Apr 2019",
        "Lease Years": "8",
        "Current Rent": "4490.3",
    },
    {
        "Tenant Name": "Clint Barton",
        "Lease Start Date": "01 Mar 2000",
        "Lease End Date": "25 May 2022",
        "Lease Years": "22",
        "Current Rent": "1234567.00",
    },
    {
        "Tenant Name": "Loki",
        "Lease Start Date": "02 May 2002",
        "Lease End Date": "25 Apr 2012",
        "Lease Years": "10",
        "Current Rent": "370680.00",
    }
]
CURRENT_RENT_EXPECTED = [
    {
        "Tenant Name": "Bruce Banner",
        "Lease Start Date": "13 Jun 2008",
        "Lease End Date": "25 Apr 2019",
        "Lease Years": "11",
        "Current Rent": "264.8",
    },
    {
        "Tenant Name": "Steve Rodgers",
        "Lease Start Date": "02 May 1944",
        "Lease End Date": "25 Apr 2012",
        "Lease Years": "68",
        "Current Rent": "370.68",
    },
    {
        "Tenant Name": "Tony Stark",
        "Lease Start Date": "01 Mar 1963",
        "Lease End Date": "25 May 1988",
        "Lease Years": "25",
        "Current Rent": "3900.00",
    },
    {
        "Tenant Name": "Point Break",
        "Lease Start Date": "27 Apr 2011",
        "Lease End Date": "25 Apr 2019",
        "Lease Years": "8",
        "Current Rent": "4490.3",
    },
    {
        "Tenant Name": "Tony Stank",
        "Lease Start Date": "26 Apr 2016",
        "Lease End Date": "25 Apr 2023",
        "Lease Years": "7",
        "Current Rent": "11530.64",
    },
]
LEASE_YEARS_EXPECTED = [
    {
        "Tenant Name": "Tony Stark",
        "Lease Start Date": "01 Mar 1963",
        "Lease End Date": "25 May 1988",
        "Lease Years": "25",
        "Current Rent": "3900.00",
    }
]
TOTAL_RENT_EXPECTED = 3900.00
MASTS_PER_EXPECTED = {
    "Black Widow": 1,
    "Bruce Banner": 1,
    "Clint Barton": 1,
    "Loki": 1,
    "Point Break": 1,
    "Steve Rodgers": 1,
    "Tony Stank": 1,
    "Tony Stark": 2
}
LEASE_START_EXPECTED = [
    {
        "Tenant Name": "Clint Barton",
        "Lease Start Date": "01/03/2000",
        "Lease End Date": "25/05/2022",
        "Lease Years": "22",
        "Current Rent": "1234567.00",
    },
    {
        "Tenant Name": "Loki",
        "Lease Start Date": "02/05/2002",
        "Lease End Date": "25/04/2012",
        "Lease Years": "10",
        "Current Rent": "370680.00",
    },
]



class TestPhoneMasts(TestCase):
    def setUp(self):
        self.PhoneMasts = PhoneMasts()

    def _setup_mock(self):
        mock_csv_reader = Mock()
        mock_csv_reader.return_value = SUCCESS_TEST_DATA
        self.PhoneMasts.make_csv_reader = mock_csv_reader

    def test_current_rent_success(self):
        self._setup_mock()

        result = self.PhoneMasts.current_rent()
        self.assertEqual(CURRENT_RENT_EXPECTED, result)
    
    def test_lease_years_success(self):
        self._setup_mock()

        result = self.PhoneMasts.lease_years()
        self.assertEqual(LEASE_YEARS_EXPECTED, result)
    
    def test_total_rent_success(self):
        self._setup_mock()

        result = self.PhoneMasts.total_rent()
        self.assertEqual(TOTAL_RENT_EXPECTED, result)
    
    def test_masts_per_tenant_success(self):
        self._setup_mock()

        result = self.PhoneMasts.masts_per_tenant()
        self.assertEqual(MASTS_PER_EXPECTED, result)
    
    def test_lease_start_date_success(self):
        self._setup_mock()

        result = self.PhoneMasts.lease_start_date()
        self.assertEqual(LEASE_START_EXPECTED, result)
