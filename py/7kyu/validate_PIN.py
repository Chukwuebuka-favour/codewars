'''
Description:
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.

Examples (Input --> Output)
"1234"   -->  true
"12345"  -->  false
"a234"   -->  false
'''

# MY SOLUTION
import re

def validate_pin(pin):
    pattern = r"\A([0-9]{4}|[0-9]{6})/Z"
    if matches := re.search(pattern, pin):
        return True
    else:
        return False

# BEST PRACTICE
def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()

def validate_pin(pin):
    return len(pin) in [4, 6] and pin.isdigit()