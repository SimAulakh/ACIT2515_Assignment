from unittest import TestCase
from hotel_staff import HotelStaff
import inspect
import datetime


class TestStaff(TestCase):
    """Unit Test class for Hotel Staff"""

    def setUp(self):
        """Creates a test fixture before each test method is run"""
        date_started = datetime.datetime.strptime("2016-01-01", "%Y-%m-%d")
        self.employee_1 = HotelStaff("Desh", "Singh", 181, "678 85A Delta, BC", 6048128090, date_started, "Manager",
                                     10000.00)
        self.employee_2 = HotelStaff("Bronwyn", "Lapadulla", 121, "7890 123 Street Surrey, BC", 7788800190,
                                     date_started,  "Manager", 15500.00)
        self.assertIsNotNone(self.employee_1, self.employee_2)
        self.logPoint()

    def tearDown(self):
        self.logPoint()

    def logPoint(self):
        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))

    def test_staff(self):
        """010A - Valid construction"""
        self.assertIsNotNone(self.employee_1, "Employee must be defined")

    def test_employee_invalid_parameters(self):
        """010B - Invalid Construction Parameters"""

        # Must reject undefined student attributes
        undefined_fname = None
        undefined_lname = None
        undefined_id = None
        undefined_address = None
        undefined_phone = None
        undefined_position = None
        undefined_date_started = None
        undefined_salary = None

        self.assertRaisesRegex(ValueError, "cannot be undefined", HotelStaff, undefined_fname, undefined_lname,
                               undefined_id, undefined_address, undefined_phone, undefined_position,
                               undefined_date_started, undefined_salary)

        # Must reject empty student attributes
        empty_fname = ""
        empty_lname = ""
        empty_id = ""
        empty_address = ""
        empty_phone = ""
        empty_position = ""
        empty_date_started = ""
        empty_salary = ""

        self.assertRaisesRegex(ValueError, "cannot be empty.", HotelStaff, empty_fname, empty_lname, empty_id,
                               empty_address, empty_phone, empty_position, empty_date_started, empty_salary)

    def test_date_started(self):
        """020A - Returns valid starting date"""
        self.assertIsNotNone(self.employee_1.get_date_started(), "Starting date must be defined")

    def test_get_position(self):
        """030A - Returns valid position"""
        self.assertIsNotNone(self.employee_2.get_position(), "Position must be defined")

    def test_get_salary(self):
        """040A - gets valid salary"""
        self.assertIsNotNone(self.employee_2.get_salary(), "Bill must be defined")

    def test_get_type(self):
        """050A - Returns valid Hotel Member type"""
        self.assertIsNotNone(self.employee_1.get_type(), "Hotel type should be defined")

    def test_get_details(self):
        """060A - Returns valid Hotel staff details"""
        self.assertIsNotNone(self.employee_2.get_details(), "Object values must be defined")
        self.assertIsNotNone(self.employee_1.get_details(), "Object values must be defined")


