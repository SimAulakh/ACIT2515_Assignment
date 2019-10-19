import datetime
from abstract_member import AbstractMember


class HotelStaff(AbstractMember):
    """Hotel Staff  Class - Child class of Abstract Member : maintains hotel staff details"""

    HOTEL_MEMBER = "staff"
    POSITION = "position"

    def __init__(self, first_name, last_name, member_id, address, phn_no, date_started, position, salary):
        super().__init__(first_name, last_name, member_id, address, phn_no)

        if date_started is None or type(date_started) != datetime.datetime:
            raise ValueError("Date cannot be none or invalid")
        self._date_started = date_started

        HotelStaff._string_input_validation(HotelStaff.POSITION, position)
        self._position = position

        if salary is None or type(salary) != float:
            raise ValueError("Salary cannot be none or invalid")
        self._salary = salary

    def get_date_started(self):
        """Returns the date the hotel employee joined"""
        return self._date_started

    def get_position(self):
        """Returns the position of the hotel employee"""
        return self._position

    def get_salary(self):
        """Returns the salary of the hotel employee"""
        return self._salary

    def set_salary(self, new_salary):
        """Returns the new salary of the hotel employee"""
        self._salary = new_salary
        return self._salary

    def get_type(self):
        """Returns the type of hotel member"""
        return self.HOTEL_MEMBER

    def get_details(self):
        """Returns the details for hotel staff"""
        details = "%s %s with member id %d working as a %s, joined on %s \n Personal information: \n Salary: %.2f \n Phone number: %s \n Address: %s" \
            % (self._first_name, self._last_name, self._member_id, self._position,
               self._date_started.strftime("%Y-%m-%d"), self._salary, self._phn_no, self._address)
        return details

    @classmethod
    def _string_input_validation(cls, position, str_value):
        """ Private helper to validate string values """

        if str_value is None:
            raise ValueError(position + " cannot be undefined.")

        if str_value == "":
            raise ValueError(position + " cannot be empty.")
