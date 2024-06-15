from ComparisonMark import *


class Countable:
    def __init__(self, count: int):
        self.__count = count

    def get_count(self):
        return self.__count

    def set_count(self, count):
        self.__count = count

    count = property(get_count, set_count)


class Condition:
    def __init__(self, input_value, comparison_mark: ComparisonMark, comparison_value):
        self.__input_value = input_value
        self.__comparison_mark = comparison_mark
        self.__comparison_value = comparison_value

    def get_input_value(self):
        return self.__input_value

    def set_input_value(self, input_value):
        self.__input_value = input_value

    def get_comparison_mark(self):
        return self.__comparison_mark

    def set_comparison_mark(self, comparison_mark):
        self.__comparison_mark = comparison_mark

    def get_comparison_value(self):
        return self.__comparison_value

    def set_comparison_value(self, comparison_value):
        self.__comparison_value = comparison_value

    input_value = property(get_input_value, set_input_value)
    comparison_mark = property(get_comparison_mark, set_comparison_mark)
    comparison_value = property(get_comparison_value, set_comparison_value)
