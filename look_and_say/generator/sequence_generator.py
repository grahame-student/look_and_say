from itertools import groupby


class SequenceGenerator:
    def __init__(self, start_value):
        """
        Constructor for the SequenceGenerator class

        :param start_value: The initial value to start the sequence from
        :type  start_value: int
        """
        self.__initial = f"{start_value}"
        self.__next = self.__initial

    def next_value(self):
        """
        Return the next value in the look and see sequence

        :return: Returns the next value in the look and see sequence
        :rtype:  string
        """
        result = self.__next
        self.__next = self.__get_next_value()

        return result

    def __get_next_value(self):
        # split __next into chunks of the same value
        chunks = SequenceGenerator.__split(self.__next)

        # convert chunks into l_&_s format
        chunks = self.__to_ls_format(chunks)

        # join chunks together
        return ''.join(chunks)

    @staticmethod
    def __split(input_text):
        return [''.join(g) for k, g in groupby(input_text)]

    @staticmethod
    def __to_ls_format(chunk_list):
        result = []
        for chunk in chunk_list:
            result.append(f"{len(chunk)}{chunk[0]}")
        return result
