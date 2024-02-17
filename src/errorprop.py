import numpy as np
import functools

from rounding import *
from constants import PLUS_MINUS

def arithmetic_decorator(binop):
    @functools.wraps(binop)
    def wrapper(lhs, rhs):
        result = ErrorProp(lhs.value, lhs.error)  # Create a new instance to hold the result
        if isinstance(rhs, ErrorProp):
            result.value = binop(lhs.value, rhs.value)
            result.error = binop(lhs.error, rhs.error)
        else:
            result.value = binop(lhs.value, rhs)
            result.error = lhs.error  # Keep the error of the original value
        return result

    return wrapper

impl_prop = {
    "__add__": lambda x, y: np.sqrt(x*x + y*y),
    # Add more operations as needed
}

# Wrap lambda functions with the arithmetic_decorator
for operation_name, operation_impl in impl_prop.items():
    impl_prop[operation_name] = arithmetic_decorator(operation_impl)

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

# Apply the decorator to each operation directly
for operation_name, operation_impl in impl_prop.items():
    setattr(ErrorProp, operation_name, operation_impl)

