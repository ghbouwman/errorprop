from rounding import *



   def __str__(self):
        
        value_magnitude = magnitude(value)
        error_magnitude = magnitude(error)

        value_part = f"{significant_digit(self.value) * 10**(magnitude-error_magnitude):.0f}"
        error_part = f"{error_significant_digit(self.error)}"
        magnitude_part = f" * 10^{error_magnitude:.0f}"

        return '(' + value_part + PLUS_MINUS + error_part + ')' + magnitude_part

