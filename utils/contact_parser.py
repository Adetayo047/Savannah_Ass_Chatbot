import re

def extract_contact_info(message):
    """Extract contact information from message using regex."""
    full_name_match = re.search(r"(Full Name|fullname|name|full_name|Full_Name):\s*([^\n,.]+)", message, re.IGNORECASE)
    email_match = re.search(r"(Email|email|email address|email_address|Email_Address):\s*([^\n,]+)", message, re.IGNORECASE)
    phone_number_match = re.search(r"(Phone Number|phone number|phone|phonenumber|phone_number|Phone_Number):\s*([^\n,.]+)", message, re.IGNORECASE)

    return {
        'Full_Name': full_name_match.group(2) if full_name_match else None,
        'Email': email_match.group(2) if email_match else None,
        'Phone_Number': phone_number_match.group(2) if phone_number_match else None
    }
    