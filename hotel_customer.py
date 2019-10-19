import datetime
from abstract_member import AbstractMember


class HotelCustomer(AbstractMember):
    """Hotel Customer  Class - Child class of Abstract Member : maintains hotel customer details"""

    HOTEL_CUSTOMER = "hotel customer"

    def __init__(self, first_name, last_name, member_id, address, phn_no, check_in, bill):
        super().__init__(first_name, last_name, member_id, address, phn_no)

        if check_in is None or type(check_in) != datetime.datetime:
            raise ValueError("Date cannot be none or invalid")
        self._check_in = check_in

        self._check_out = None

        if bill is None or type(bill) != float:
            raise ValueError("Salary cannot be none or invalid")
        self._bill = bill

    def get_check_in_date(self):
        """Returns the date the customer checked in"""
        return self._check_in

    def get_bill(self):
        """Returns the total bill for the customer"""
        return self._bill

    def set_bill(self, bill):
        """Returns the new salary of the hotel employee"""
        self._bill = bill
        return self._bill

    def get_type(self):
        """Returns the type of hotel member"""
        return self.HOTEL_CUSTOMER

    def get_details(self):
        """Returns the details for hotel staff"""
        details = "%s %s with member id %d checked in on %s . Total bill : %.2f \n Personal information: \n Phone_number: %.2f \n Address: %s" \
            % (self._first_name, self._last_name, self._member_id, self._check_in.strftime("%Y-%m-%d")
               , self._bill, self._phn_no, self._address)
        return details
