# ✉️ Email Validation with MX Record Lookup 📬

**Tired of bouncing emails and undeliverable addresses clogging up your system?** This Python utility is your solution! It not only checks the validity of an email address format but also ensures the domain is real and ready to accept emails via MX (Mail Exchange) record lookups. Integrate this tool seamlessly into any Django project to enhance your email validation process. ✅

## 🚀 Features

- **Format Validation**: Leverages Django's powerful built-in validator to ensure the email follows the correct syntax.
- **Domain Verification**: Uses MX record checks to confirm that the domain can actually receive emails (no more `invalid@nope.com`!).
- **Smooth Error Handling**: Provides meaningful error messages for invalid emails, making troubleshooting a breeze.

## 🛠️ Installation

### 📦 Dependencies

To get started, install the necessary packages. These are the engines that drive the email validation magic!

```bash
pip install git+https://github.com/rthalley/dnspython.git
pip install dnspython
pip install email-validator
```

### 🔧 Running the Script

You can validate your email addresses in seconds. Simply run the provided script and watch it in action as it checks both the format and deliverability of the email addresses.

```bash
python email_validator_script.py
```

### 📝 Example Usage

The `check_email_validity` function performs two key tasks:
1. Verifies that the email address is syntactically correct.
2. Ensures the email domain is active and has valid MX records.

#### 🧑‍💻 Python Code Example

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

### 🔍 Example Output

```bash
test@gmail.com is a valid email address.
invalid@invalid.com is not a valid email address.
```

## 🤔 How Does It Work?

1. **Email Format Validation**: First, the email is checked using Django’s `validate_email` function to ensure it follows a valid format.
2. **Domain Check (MX Record Lookup)**: Next, the `email-validator` package confirms whether the domain is configured to accept emails by performing a DNS lookup for MX records.
3. **Error Handling**: If something goes wrong—whether it’s an invalid format or a domain that doesn’t accept mail—you get a clear, actionable error message.

## 💻 Requirements

- **Python**: Version 3.x and above
- **Django**: For its built-in email validation feature
- **Packages**: 
  - `email-validator`
  - `dnspython`

## 🌍 Contributing

We welcome all contributions! 🎉 Feel free to fork the repository, improve the code, or even suggest new features by submitting pull requests. Let’s make email validation rock-solid together! 🤝

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

### ✨ Key Highlights:

- **User-friendly**: Describes the functionality in an engaging way.
- **Step-by-step guide**: Clear instructions on how to install and use the script, including example code and output.
- **Open for Contributions**: Encourages collaboration from the GitHub community.
- **Fun & Engaging Tone**: Makes the project approachable and gives it a modern, friendly vibe.

