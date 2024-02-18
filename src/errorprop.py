import numpy as np
import functools

from rounding import *
from constants import PLUS_MINUS

class ErrorProp:

    def __init__(self, value, error=0.0):

        self.value = value

        assert error >= 0
        self.error = error

    def relative(self):
        
        return self.error / self.value

    def __add__(self, other):

        rv = ErrorProp(self.value, self.error)

        if isinstance(other, ErrorProp):
            rv.value += other.value
            rv.error = np.sqrt(self.error**2 + other.error**2)

        else:
            rv.value += other

        return rv

    def __radd__(self, other):

        return self.__add__(other)

    def __sub__(self, other):

        rv = ErrorProp(self.value, self.error)

        if isinstance(other, ErrorProp):
            rv.value -= other.value
            rv.error = np.sqrt(self.error**2 + other.error**2)

        else:
            rv.value -= other

        return rv

    def __rsub__(self, other):

        return -1 * self.__sub__(other)

    def __mul__(self, other):

        rv = ErrorProp(self.value, self.error)

        if isinstance(other, ErrorProp):
            rv.value *= other.value
            rv.error = np.abs(rv.value) * np.sqrt(self.relative()**2 + other.relative()**2)

        else:
            rv.value *= other

        return rv

    def __rmul__(self, other):

        return self.__mul__(other)

    def __truediv__(self, other):

        rv = ErrorProp(self.value, self.error)
    
        if isinstance(other, ErrorProp):
            rv.value /= other.value
            rv.error = np.abs(rv.value) * np.sqrt(self.relative()**2 + other.relative()**2)

        else:
            rv.value *= other

        return rv

    def __rtruediv__(self, other):

        return ErrorProp(1) / self.__div__(other)

    def __pow__(self, other):

        rv = ErrorProp(self.value, self.error)
        rv.value = self.value ** other
        rv.error = rv.value * other * self.relative()
        return rv

    def __neg__(self):
        
        rv = ErrorProp(self.value, self.error)
        rv.value *= -1
        return rv
    
    def __abs__(self):
        
        rv = ErrorProp(self.value, self.error)
        rv.value = abs(rv.value)
        return rv

    def __repr__(self):

        return f"ErrorProp(value={self.value}, error={self.error})"

    def __str__(self):
        
        value_magnitude = magnitude(self.value)
        error_magnitude = magnitude(self.error)

        value_part = f"{self.value * 10**-error_magnitude:.0f}"
        error_part = f"{error_significant_digit(self.error)}"
        magnitude_part = f" * 10^{error_magnitude:.0f}"

        return '(' + value_part + PLUS_MINUS + error_part + ')' + magnitude_part

