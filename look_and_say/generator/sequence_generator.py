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
        Return the next value in the look and say sequence

        :return: Returns the next value in the look and say sequence
        :rtype:  string
        """
        result = self.__next
        self.__next = self.__get_next_value()

        return result

    def __get_next_value(self):
        """
        Calculate the next value in the look and say sequence

        :return: Returns the next value in the look and say sequence
        :rtype:  string
        """
        # split __next into chunks of the same value
        chunks = SequenceGenerator.__split(self.__next)

        # convert chunks into l_&_s format
        chunks = self.__to_ls_format(chunks)

        # join chunks together
        return "".join(chunks)

    @staticmethod
    def __split(input_text):
        """
        Split the input text each time the character in the input changes

        | examples:
        |    "123"  -> ["1", "2", "3"]
        |    "1121" -> ["11", "2", "1"]

        :param input_text: The text to split into groups
        :type  input_text: string

        :return: list of strings
        """
        return ["".join(g) for k, g in groupby(input_text)]

    @staticmethod
    def __to_ls_format(chunk_list):
        """
        Converts each chunk in the list to the look and say format

        | examples:
        |    ["1"]            -> ["11"]
        |    ["11", "2", "1"] -> ["21", "12", "11"]

        :param chunk_list: chunks to be converted to look and say format
        :type  chunk_list: list of strings

        :return: list of look and say formatted chunks
        :rtype:  list of strings
        """
        result = []
        for chunk in chunk_list:
            result.append(f"{len(chunk)}{chunk[0]}")
        return result
