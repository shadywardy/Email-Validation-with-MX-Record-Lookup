### Email Validation with MX Record Lookup

This project provides a Python utility to validate email addresses, checking both the format and domain deliverability using MX record lookups. The script can be integrated into Django applications and uses both Django's built-in validators and external libraries for domain validation.

## Features

- Validate email format using Django's built-in email validator.
- Check if the domain of the email has valid DNS MX records (i.e., is deliverable).
- Simple and efficient error handling for invalid email addresses.

## Installation

### Dependencies

The project relies on the `email-validator` package and `dnspython` for validating email domains via DNS MX records. Ensure these dependencies are installed by running the following commands:

```bash
pip install git+https://github.com/rthalley/dnspython.git
pip install dnspython
pip install email-validator
```

### Running the Script

You can test the email validation function by running the provided script. The script checks the format and deliverability of two example email addresses.

```bash
python email_validator_script.py
```

### Example Usage

The `check_email_validity` function validates both the format and MX record of the provided email. If the email passes both checks, it is deemed valid.

#### Example Python Code

```python
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
```

### Example Output

```bash
test@gmail.com is a valid email address.
invalid@invalid.com is not a valid email address.
```

## How It Works

1. **Email Format Validation**: The email format is first validated using Django's `validate_email` function, which ensures that the email follows a standard email format.
2. **MX Record Lookup**: The domain of the email is checked for valid MX (Mail Exchange) records using `email-validator`, which utilizes `dnspython` for DNS lookups.
3. **Error Handling**: If either the format or domain is invalid, the script returns an appropriate error message indicating the issue.

## Requirements

- Python 3.x
- Django (for built-in email validation)
- `email-validator` and `dnspython` packages

## Contributing

Feel free to fork this repository and submit pull requests for improvements or additional features.

## License

This project is licensed under the MIT License.

