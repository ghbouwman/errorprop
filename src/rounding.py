import numpy as np

def significant_digit(value):
    
    for char in str(value):
        
        if char not in "0.":
            return int(char)

def error_significant_digit(error):

    digit = significant_digit(error)
    
    # Check if the number is exact, since that does require rounding up.
    non_zero_digits = str(error)\
                      .replace('0', '')\
                      .replace('.', '')
                        
    exact = len(non_zero_digits) <= 1 # Less than because e.g. 0.0 is exact.
        
    if not exact:

        # Round up
        digit += 1

    return digit


def round_error(error):
    """

    """
    error_str = str(error)


    for char in error_str:
        if char not in "0.":
            significant_digit = int(char)
            break

    exact = len(error_str.replace('0', '').replace('.', '')) <= 1

    if not exact:
        significant_digit += 1

    magnitude = int(np.floor(np.log10(error)))
    
    return significant_digit, magnitude

