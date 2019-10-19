from unittest import TestCase
from hotel_customer import HotelCustomer
import inspect
import datetime


class TestCustomer(TestCase):
    """Unit Test class for Hotel Customer"""

    def setUp(self):
        """Creates a test fixture before each test method is run"""
        check_in = datetime.datetime.strptime("2016-01-01", "%Y-%m-%d")
        self.customer_1 = HotelCustomer("Simrat", "Kaur", 100, "678 85A Delta, BC", 6048898090, check_in, 1000.00)
        self.customer_2 = HotelCustomer("Neha", "Kakkar", 120, "7890 123 Street Surrey, BC", 7788898190, check_in, 550.00)
        self.assertIsNotNone(self.customer_1, self.customer_2)
        self.logPoint()

    def tearDown(self):
        self.logPoint()

    def logPoint(self):
        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))

    def test_customer(self):
        """010A - Valid construction"""
        self.assertIsNotNone(self.customer_1, "Customer must be defined")

    def test_customer_invalid_parameters(self):
        """010B - Invalid Construction Parameters"""

        # Must reject undefined student attributes
        undefined_fname = None
        undefined_lname = None
        undefined_id = None
        undefined_address = None
        undefined_phone = None
        undefined_check_in = None
        undefined_bill = None
        self.assertRaisesRegex(ValueError, "cannot be undefined", HotelCustomer, undefined_fname, undefined_lname,
                               undefined_id, undefined_address, undefined_phone, undefined_check_in, undefined_bill)

        # Must reject empty student attributes
        empty_fname = ""
        empty_lname = ""
        empty_id = ""
        empty_address = ""
        empty_phone = ""
        empty_check_in = ""
        empty_bill = ""
        self.assertRaisesRegex(ValueError, "cannot be empty.", HotelCustomer, empty_fname, empty_lname, empty_id,
                               empty_address, empty_phone, empty_check_in, empty_bill)

    def test_check_in_date(self):
        """020A - Returns valid check_in date"""
        self.assertIsNotNone(self.customer_1.get_member_id(), "Member id must be defined")

    def test_get_bill(self):
        """030A - Returns valid bill"""
        self.assertIsNotNone(self.customer_1.get_bill(), "Bill must be defined")

    def test_valid_set_bill(self):
        """040A - Sets valid bill"""
        self.customer_2.set_bill(600.00)
        self.assertIsNotNone(self.customer_2.get_bill(), "Bill must be defined")

    def test_get_type(self):
        """050A - Returns valid Hotel Member type"""
        self.assertIsNotNone(self.customer_1.get_type(), "Hotel type should be defined")

    def test_get_details(self):
        """060A - Returns valid Hotel Customer details"""
        self.assertIsNotNone(self.customer_1.get_details(), "Object values must be defined")
        self.assertIsNotNone(self.customer_2.get_details(), "Object values must be defined")


