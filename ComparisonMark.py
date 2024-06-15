from abc import ABC, abstractmethod


class ComparisonMark(ABC):
    @abstractmethod
    def return_mark(self): pass


class Equal(ComparisonMark):
    def return_mark(self):
        return "Equal"


class Less(ComparisonMark):
    def return_mark(self):
        return "Less"


class Greater(ComparisonMark):
    def return_mark(self):
        return "Greater"


class NotEqual(ComparisonMark):
    def return_mark(self):
        return "NotEqual"


class GreaterEqual(ComparisonMark):
    def return_mark(self):
        return "GreaterEqual"


class LessEqual(ComparisonMark):
    def return_mark(self):
        return "LessEqual"
