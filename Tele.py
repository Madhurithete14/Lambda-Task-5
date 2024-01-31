# Problem : Using Python Regular Expression, Telephone number of USA

import re


def validate_usa_mobile_number(mobile_number):
    pattern = "^(\\+\\d{1,3}( )?)?((\\(\\d{3}\\))|\\d{3})[- .]?\\d{3}[- .]?\\d{4}$"
    result = re.search(pattern, mobile_number)
    if result:
        return "SUCCESS : USA Telephone Number is valid"
    else:
        return "ERROR : Invalid Mobile Number"
   
mobile_number = "+111 (202) 555-0125"


print(validate_usa_mobile_number(mobile_number))
