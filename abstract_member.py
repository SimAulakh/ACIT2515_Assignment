
class AbstractMember:
    """ Abstract Member Class - Maintains the details of hotel members"""

    FIRST_NAME_LABEL = "First Name"
    LAST_NAME_LABEL = "Last Name"
    ADDRESS_LABEL = "Address"
    PHONE_LABEL = "Phone Number"

    def __init__(self, first_name, last_name, member_id, address, phn_no):
        """Constructor - Initialize the data values"""

        AbstractMember._validate_string_input(AbstractMember.FIRST_NAME_LABEL, first_name)
        self._first_name = first_name

        AbstractMember._validate_string_input(AbstractMember.LAST_NAME_LABEL, last_name)
        self._last_name = last_name

        if member_id is None or type(member_id) != int:
            raise ValueError("Member id is invalid")
        self._member_id = member_id

        AbstractMember._validate_string_input(AbstractMember.ADDRESS_LABEL, address)
        self._address = address

        AbstractMember._validate_string_input(AbstractMember.PHONE_LABEL, phn_no)
        self._phn_no = phn_no

    def get_type(self):
        """Gets the type of hotel member"""
        raise NotImplementedError("Child class must implement")

    def get_member_id(self):
        """Gets the ID of hotel members"""
        return self._member_id

    def set_member_id(self, new_id):
        """Gets the ID of hotel members"""
        self._member_id = new_id
        return self._member_id

    def get_first_name(self):
        """Gets the first name of a member"""
        return self._first_name

    def get_last_name(self):
        """Gets the first name of a member"""
        return self._last_name

    def get_full_name(self):
        """Returns the full name of a member"""
        return self._first_name + " " + self._last_name

    def get_address(self):
        """Returns the address of the hotel members"""
        return self._address

    def get_phn_no(self):
        """Returns the phone number of the hotel members"""
        return self._phn_no

    def get_details(self):
        """Returns the details of the hotel members according to their type"""
        raise NotImplementedError("Child class must implement the details")

    @classmethod
    def _validate_string_input(cls, display_name, str_value):
        """ Private helper to validate string values """

        if str_value is None:
            raise ValueError(display_name + " cannot be undefined.")

        if str_value == "":
            raise ValueError(display_name + " cannot be empty.")
