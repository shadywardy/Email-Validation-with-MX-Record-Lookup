
from email_validator import validate_email, EmailNotValidError
from django.core.validators import validate_email as django_validate_email
from django.core.exceptions import ValidationError

def check_email_validity(email):
    # Step 1: Validate email format using Django's built-in validator
    try:
        django_validate_email(email)
        is_valid_format = True
    except ValidationError:
        is_valid_format = False

    # Step 2: Validate email domain using email-validator
    try:
        validation = validate_email(email, check_deliverability=True)
        is_valid_domain = True
    except EmailNotValidError as e:
        is_valid_domain = False

    if is_valid_format and is_valid_domain:
        return f"{email} is a valid email address."
    else:
        return f"{email} is not a valid email address."

# Test the function
if __name__ == "__main__":
    email1 = "test@gmail.com"
    email2 = "invalid@invalid.com"

    print(check_email_validity(email1))
    print(check_email_validity(email2))
