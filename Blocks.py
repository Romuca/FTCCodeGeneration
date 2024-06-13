from abc import ABC, abstractmethod
from math import pi


class Block(ABC):
    @abstractmethod
    def type(self): pass


class ComparisonMark(ABC):
    @abstractmethod
    def return_mark(self): pass


class Equal(ComparisonMark):
    def return_mark(self):
        return "Equal"


class Smaller(ComparisonMark):
    def return_mark(self):
        return "Smaller"


class Bigger(ComparisonMark):
    def return_mark(self):
        return "Bigger"


class NotEqual(ComparisonMark):
    def return_mark(self):
        return "NotEqual"


class BiggerEqual(ComparisonMark):
    def return_mark(self):
        return "BiggerEqual"


class SmallerEqual(ComparisonMark):
    def return_mark(self):
        return "SmallerEqual"


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


class Unit(ABC):
    @abstractmethod
    def return_k(self): pass


class Centimeter(Unit):
    k = 1

    def return_k(self):
        return self.k


class Ticks(Unit):
    k = None

    def __init__(self, tpr: float, wheel_diameter: float):
        self.__tpr = tpr
        self.__wheel_diameter = wheel_diameter
        self.k = self.__tpr / (pi * self.__wheel_diameter)

    def get_wheel_d(self):
        return self.__wheel_diameter

    def set_wheel_d(self, wheel_diameter):
        self.__wheel_diameter = wheel_diameter
        self.k = self.__tpr / (pi * self.__wheel_diameter)

    def get_tpr(self):
        return self.__tpr

    def set_tpr(self, tpr):
        self.__tpr = tpr
        self.k = self.__tpr / (pi * self.__wheel_diameter)

    wheel_diameter = property(get_wheel_d, set_wheel_d)
    tpr = property(get_tpr, set_tpr)

    def return_k(self):
        return self.k


class Degrees(Unit):
    angle_k = 1

    def return_k(self):
        return self.angle_k


class Radians(Unit):
    angle_k = 180 / pi

    def return_k(self):
        return self.angle_k


class MoveStraight(Block):
    def type(self):
        return "MoveStraight"

    def __init__(self, units: Unit, quantity: int, power: float):
        self.__units = units
        self.__quantity = quantity
        self.__power = power

    def get_units(self):
        return self.__units

    def set_units(self, units):
        self.__units = units

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def get_power(self):
        return self.__power

    def set_power(self, power):
        self.__power = power

    units = property(get_units, set_units)
    quantity = property(get_quantity, set_quantity)
    power = property(get_power, set_power)


class Rotate(Block):
    def type(self):
        return "Rotate"

    def __init__(self, units: Unit, quantity: int, power: float):
        self.__units = units
        self.__quantity = quantity
        self.__power = power

    def get_units(self):
        return self.__units

    def set_units(self, units):
        self.__units = units

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def get_power(self):
        return self.__power

    def set_power(self, power):
        self.__power = power

    units = property(get_units, set_units)
    quantity = property(get_quantity, set_quantity)
    power = property(get_power, set_power)


class MoveToPoint(Block):
    def type(self):
        return "MoveToPoint"

    def __init__(self, power: float, x: float, y: float):
        self.__power = power
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = y

    def get_power(self):
        return self.__power

    def set_power(self, power):
        self.__power = power

    x = property(get_x, set_x)
    y = property(get_y, set_y)
    power = property(get_power, set_power)


class ControlServo(Block):
    def type(self):
        return "ControlServo"

    def __init__(self, name: str, position: float):
        self.__position = position
        self.__name = name

    def get_position(self):
        return self.__position

    def set_position(self, position):
        self.__position = position

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    position = property(get_position, set_position)
    name = property(get_name, set_name)


class ControlCRServo(Block):
    def type(self):
        return "ControlCRServo"

    def __init__(self, name: str, power: float, seconds: float):
        self.__power = power
        self.__name = name
        self.__seconds = seconds

    def get_power(self):
        return self.__power

    def set_power(self, power):
        self.__power = power

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_seconds(self):
        return self.__seconds

    def set_seconds(self, seconds):
        self.__seconds = seconds

    power = property(get_power, set_power)
    name = property(get_name, set_name)
    seconds = property(get_seconds, set_seconds)


class TelemetryAddData(Block):
    def type(self):
        return "TelemetryAddData"

    def __init__(self, value: str, caption: str):
        self.__caption = caption
        self.__value = value

    def get_caption(self):
        return self.__caption

    def set_caption(self, caption):
        self.__caption = caption

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value

    caption = property(get_caption, set_caption)
    value = property(get_value, set_value)


class Sleep(Block):
    def type(self):
        return "Sleep"

    def __init__(self, seconds: float):
        self.__seconds = seconds

    def get_seconds(self):
        return self.__seconds

    def set_seconds(self, seconds):
        self.__seconds = seconds

    seconds = property(get_seconds, set_seconds)


class GetDistance(Block):
    def type(self):
        return "GetDistance"

    def __init__(self, name: str, units: Unit):
        self.__units = units
        self.__name = name

    def get_units(self):
        return self.__units

    def set_units(self, units):
        self.__units = units

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    units = property(get_units, set_units)
    name = property(get_name, set_name)


class Loop(Block):
    def type(self):
        return "Loop"

    def __init__(self, class_type, actions: list):
        self.__actions = actions
        self.__class_type = class_type

    def get_actions(self):
        return self.__actions

    def set_actions(self, actions):
        self.__actions = actions

    def get_class_type(self):
        return self.__class_type

    def set_class_type(self, class_type):
        self.__class_type = class_type

    actions = property(get_actions, set_actions)
    class_type = property(get_class_type, set_class_type)


class If(Block):
    def type(self):
        return "If"

    def __init__(self, class_type: Condition, actions: list, else_actions: list):
        if class_type is not Condition:
            raise TypeError
        self.__actions = actions
        self.__else_actions = else_actions
        self.__class_type = class_type

    def get_actions(self):
        return self.__actions

    def set_actions(self, actions):
        self.__actions = actions

    def get_else_actions(self):
        return self.__else_actions

    def set_else_actions(self, else_actions):
        self.__else_actions = else_actions

    def get_class_type(self):
        return self.__class_type

    def set_class_type(self, class_type):
        self.__class_type = class_type

    actions = property(get_actions, set_actions)
    else_actions = property(get_else_actions, set_else_actions)
    class_type = property(get_class_type, set_class_type)


block1 = Loop(  # example
    Condition(123, Equal, 123),
    [
        ControlServo("asd", 0.1)
    ]
)

block2 = Loop(
    Countable(3),
    [
        MoveStraight(Centimeter, 30, 0.75),
        Sleep(5)
    ]
)

block3 = If(
    Condition(450, Bigger, 499),
    [],  # some actions
    []  # another actions
)
