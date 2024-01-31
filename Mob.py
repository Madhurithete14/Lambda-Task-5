# Problem : Using Python Regular Expression, Mobile numbers of Bangaladesh

import re


def validate_bangaladesh_mobile_number(mobile_number):
    pattern = "(?:\\+88|88)?(01[3-9]\\d{8})" 
    result = re.search(pattern, mobile_number)
    if result:
        return "SUCCESS : Bangladesh Mobile Number is valid"
    else:
        return "ERROR : Invalid Mobile Number"
   
mobile_number = "8801736458080"


print(validate_bangaladesh_mobile_number(mobile_number))
