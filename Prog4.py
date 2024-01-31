# Problem : Using Python Regular Expression, validate any email ID
import re
def validate_email_address(email_id):
    pattern = "^[a-z0-9.]+@[a-z0-9]+.+[a-z]{2,6}$"
    result = re.search(pattern, email_id)
    if result:
        return "SUCCESS : Email ID is valid"
    else:
        return "ERROR : Invalid Email ID"   
email_id = "madhurithete14@gmail.com"
print(validate_email_address(email_id))
