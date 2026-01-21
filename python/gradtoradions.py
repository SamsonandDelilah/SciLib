#
#   --- SciLib ---
#

# define imports
import numpy as np
import re
from decimal import Decimal
from gmpy2 import mpfr, const_pi

# helper function for DMS
def parse_flexible_dms(dms_string):
    """
    Parse flexible DMS format: "180°", "180°20'", "180°20'13''"
    Returns decimal degrees or None if invalid.
    """
    # Flexible DMS: 1-3 components after °
    flexible_dms = r"^(-?\d+)(°(?:\s*(\d+)'?(?:\s*(\d+)''?)?)?)?$"
    match = re.match(flexible_dms, dms_string.strip())
    
    if not match:
        return None
    
    grad = int(match.group(1))
    minuten = int(match.group(3)) if match.group(3) else 0
    sekunden = int(match.group(4)) if match.group(4) else 0
    return grad + minuten/60 + sekunden/3600


# function to convert from Grad to Radians     
def GradToRadians(x):
    """
    Converts angle inputs to radians.

    Supported input formats:
    - Decimal degrees (float, int, Decimal, BigFloat)
    - Flexible DMS: "180°", "180°20'", "180°20'13''"
    - Decimal/scientific strings: "180.57", "2.3456e1" or mpfr('180.001')

    :param x: Angle to convert. Numeric or string.
    :return: Radians (mpfr) or None on error.
    """
    error_message = None
    
    if isinstance(x, mpfr):
        x_str = str(x)
        if any(symbol in x_str for symbol in ['°', "'", '"', "'"]):
            print(f"mpfr input invalid: '{x}'. Use: mpfr('180.57') without symbols.")
            return None
    try:

        # Numeric input
        if isinstance(x, (int, float, Decimal, mpfr)):
            if isinstance(x, mpfr):
                x_str = str(x)
                if '°' in x_str:
                    raise ValueError(f"mpfr cannot parse degree symbol: {x_str}")
                decimal_value = x
            elif isinstance(x, Decimal):
                decimal_value = mpfr(str(x))
            else:
                decimal_value = mpfr(x)
            return decimal_value * const_pi() / mpfr('180')

        # String input
        elif isinstance(x, str):
            # 1. Flexible DMS
            dms_decimal = parse_flexible_dms(x)
            if dms_decimal is not None:
                return mpfr(dms_decimal) * const_pi() / mpfr('180')
            
            # 2. Decimal: "180.57"
            decimal_pattern = r"^(-?\d+(?:\.\d+)?)$"
            # 3. Scientific: "2.3456e1"
            scientific_pattern = r"^(-?\d+(?:\.\d+)?[eE][+-]?\d+)$"
            
            match_decimal = re.match(decimal_pattern, x)
            match_scientific = re.match(scientific_pattern, x)
            
            if match_decimal or match_scientific:
                return mpfr(x) * const_pi() / mpfr('180')
            
            else:
                error_message = f"Invalid format: '{x}'.\nUse: 180.57, '180°', '180°20'', '180°20'13''', 2.3456e1 or mfpr('180.0')"
        
        else:
            error_message = "Input must be numeric or string."
    
    except Exception as e:
        error_message = str(e)
    
    if error_message:
        print(error_message)
        return None

# function to convert from Radians to Grad   
def RadiansToGrad(x):
    """
    Converts radians to degrees or parses DMS to decimal degrees.
    
    Supported formats:
    - Radians (float, int, Decimal, mpfr)
    - Flexible DMS: "180°", "180°20'", "180°20'13''"
    - Decimal/scientific strings → radians → degrees

    :param x: Angle in radians or DMS string.
    :return: Degrees (mpfr) or None on error.
    """
    error_message = None
    try:
        # Numeric input (radians)
        if isinstance(x, (int, float, Decimal, mpfr)):
            if isinstance(x, mpfr):
                radian_value = x
            elif isinstance(x, Decimal):
                radian_value = mpfr(str(x))
            else:
                radian_value = mpfr(x)
            return radian_value * mpfr('180') / const_pi()

        # String input
        elif isinstance(x, str):
            # 1. Flexible DMS → direkt Degrees
            dms_decimal = parse_flexible_dms(x)
            if dms_decimal is not None:
                return mpfr(dms_decimal)
            
            # 2. Decimal/Scientific → radians → degrees
            decimal_pattern = r"^(-?\d+(?:\.\d+)?)$"
            scientific_pattern = r"^(-?\d+(?:\.\d+)?[eE][+-]?\d+)$"
            
            match_decimal = re.match(decimal_pattern, x)
            match_scientific = re.match(scientific_pattern, x)
            
            if match_decimal or match_scientific:
                return mpfr(x) * mpfr('180') / const_pi()
            
            else:
                error_message = f"Invalid format: '{x}'.\nUse: radians 3.14, 1.234e1"
        
        else:
            error_message = "Input must be numeric or string."
    
    except Exception as e:
        error_message = str(e)
    
    if error_message:
        print(error_message)
        return None


# Usage examples
if __name__ == "__main__":
    result = GradToRadians("N 180")                  # will generate error, display the error
    if result is not None:                          # and provides a 'None' value 
        s = result * 34
    else:
        print("Calculation cannot be performed.\n")

    # More examples
    print(GradToRadians(180.57))                    # Decimal degrees example
    print(GradToRadians("180.57"))                  # Decimal degrees example
    print(GradToRadians("180°20'13''"))             # DMS example
    print(GradToRadians(2.3456e1))                  # Scientific notation example
    print(GradToRadians("2.3456e1"))                # Scientific notation example
    print(GradToRadians(mpfr("180.57")))            # mpfr decimal degrees example

    print("Radians\n")

    print(RadiansToGrad(3.14))  
    print(RadiansToGrad("3.14"))  
    print(RadiansToGrad(np.pi))                     # π → 180° (mpfr)
    print(RadiansToGrad(mpfr('3.1415926535', 128))) # High precision
    print(RadiansToGrad("1.234e1"))                 # Scientific → Degrees
    print(RadiansToGrad("0.40938442")  )            # DMS → Degrees (direct)

