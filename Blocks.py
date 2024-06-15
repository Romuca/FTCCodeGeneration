from ConditionTypes import *
from Units import *


class Block(ABC):
    @abstractmethod
    def type(self): pass


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

    def __init__(self, caption: str, value):
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

    position = property(get_caption, set_caption)
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
