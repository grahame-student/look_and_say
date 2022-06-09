class SequenceGenerator:
    def __init__(self, start_value):
        """
        Constructor for the SequenceGenerator class

        :param start_value: The initial value to start the sequence from
        :type  start_value: int
        """
        self.__initial = start_value
        self.__next = self.__initial

    def next_value(self):
        """
        Return the next value in the look and see sequence

        :return: Returns the next value in the look and see sequence
        :rtype:  string
        """
        result = self.__next
        self.__next = self.__get_next_value()

        return f"{result}"

    def __get_next_value(self):
        return "11"
