def validate_username(username):
    if not isinstance(username, str):
        return "Username must be a string"

    if len(username) < 3 or len(username) > 15:
        return "Username length must be between 3 and 15"

    if not username.isalnum():
        return "Username must be alphanumeric"

    return "VALID"


def validate_age(age):
    if not isinstance(age, int):
        return "Age must be an integer"

    if age < 18 or age > 60:
        return "Age must be between 18 and 60"

    return "VALID"


def validate_email(email):
    if not isinstance(email, str):
        return "Email must be a string"

    if "@" not in email or "." not in email:
        return "Invalid email format"

    return "VALID"
