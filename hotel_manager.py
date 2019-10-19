from abstract_member import AbstractMember
from hotel_stats import HotelStats
from hotel_staff import HotelStaff
from hotel_customer import HotelCustomer
import datetime


class HotelManager:
    """Hotel Manager - Maintains all the modification of the Hotel """

    HOTEL_NAME_LABEL = "Hotel Name"

    def __init__(self, hotel_name):
        """Initializes data values"""
        HotelManager._validate_string_input(HotelManager.HOTEL_NAME_LABEL, hotel_name)
        self._hotel_name = hotel_name
        self._next_available_id = 101

        self._members = []

    def add_member(self, hotel_member):
        """Adds a new hotel employee or customer"""
        if hotel_member is None or not isinstance(hotel_member, AbstractMember):
            raise ValueError("Invalid hotel object ")
        hotel_member.set_member_id(self._next_available_id)
        self._next_available_id = self._next_available_id + 1
        self._members.append(hotel_member)
        return hotel_member.get_member_id()

    def get_members_by_id(self, member_id):
        """Gets the product by id by first checking the type of the id and after that it checks if it exists inlist """
        if member_id is None or type(member_id) != int:
            raise ValueError("Invalid member id")
        for curr_member in self._members:
            if member_id == curr_member.get_member_id():
                return curr_member
        return None

    def get_all_members(self):
        """Returns all the members of hotel"""
        if len(self._members) > 0:
            return self._members
        else:
            return None

    def get_all_members_by_type(self, member_type):
        """Returns all hotel members by type """
        if member_type is None or type(member_type) != str:
            raise ValueError("Invalid member type")
        for curr_member in self._members:
            if member_type == curr_member.get_type():
                return curr_member
        return None

    def update_member(self, member):
        """Updates the hotel member"""
        if member is None or not isinstance(member, AbstractMember):
            raise ValueError("Invalid hotel member")
        for index, p in enumerate(self._members, 0):
            if p.get_member_id() == id:
                self._members[index] = member
                return self._members

    def remove_member_by_id(self, member_id):
        """Removes the hotel member by using member id"""
        if member_id is None or type(member_id) != int:
            raise ValueError("Invalid member id")

        for curr_member in self._members:
            if member_id == curr_member.get_member_id():
                self._members.remove(curr_member)


    @staticmethod
    def _validate_string_input(display_name, string_value):
        """Validates string input"""
        if string_value is None:
            raise ValueError(display_name + " cannot be undefined.")
        if type(string_value) != str:
            raise ValueError(display_name + " should be string.")
