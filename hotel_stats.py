class HotelStats:
    """ Statistics on a Hotel"""

    def __init__(self, total_num_staff, num_customers, avg_years_employed, num_days_stayed):
        """Initializing the data values"""
        if total_num_staff is None or type(total_num_staff) != int:
            raise ValueError("Invalid value")
        self._total_num_staff = total_num_staff

        if num_customers is None or type(num_customers) != int:
            raise ValueError("Invalid value")
        self._num_customers = num_customers

        if avg_years_employed is None or type(avg_years_employed) != float:
            raise ValueError("Invalid value")
        self._avg_years_employed = avg_years_employed

        if num_days_stayed is None or type(num_days_stayed) != float:
            raise ValueError("Invalid value")
        self._num_days_stayed = num_days_stayed

    def get_total_num_staff(self):
        """Returns the total number of staff in the hotel"""
        return self._total_num_staff

    def get_num_customers(self):
        """Returns the total number of customers in the hotel"""
        return self._num_customers

    def get_avg_years_employed(self):
        """Returns the total number of staff in the hotel"""
        return self._total_num_staff

    def get_num_days_stayed(self):
        """Returns the total number of days stayed in hotel by the customer"""
        return self._num_days_stayed
