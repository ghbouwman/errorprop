import numpy as np
import functools

from rounding import *
from constants import PLUS_MINUS

class ErrorProp:

    def __init__(self, value, error=0.0):

        self.value = value
        self.error = error

    def __repr__(self):

        return f"ErrorProp(value={self.value}, error={self.error})"

    def __str__(self):
        
        magnitude = np.floor(np.log10(self.value))
        error_magnitude = np.floor(np.log10(self.error))

        value_part = f"{significant_digit(self.value)*10**(magnitude-error_magnitude):.0f}"
        error_part = f"{error_significant_digit(self.error)}"
        magnitude_part = f" * 10^{error_magnitude:.0f}"

        return '(' + value_part + PLUS_MINUS + error_part + ')' + magnitude_part

impl_dict = {}

impl_dict["__add__"] = lambda x, dx, y, dy, z: np.sqrt(dx**2 + dy**2)
impl_dict["__mul__"] = lambda x, dx, y, dy, z: np.abs(z)*np.sqrt((dx/x)**2 + (dy/y)**2)
impl_dict["__pow__"] = lambda x, dx, y, dy, z: z*y*dx/x
impl_dict["__sub__"] = impl_dict["__add__"]
impl_dict["__truediv__"] = impl_dict["__mul__"]


for op_name, propagation_impl in impl_dict.items():

    def impl(lhs, rhs):
        result = ErrorProp(lhs.value, lhs.error)  # Create a new instance to hold the result
        op = getattr(result.value, op_name)

        if isinstance(rhs, ErrorProp):
            result.value = op(rhs.value)
            result.error = propagation_impl(lhs.value, lhs.error, rhs.value, rhs.error, result.value)
        else:
            result.value = op(rhs)

        return result

    setattr(ErrorProp, op_name, impl)

