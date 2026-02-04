import csv
import pytest
from app.validator import validate_username, validate_age, validate_email


def load_test_data():
    data = []
    with open("test_data/invalid_inputs.csv") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data


@pytest.mark.parametrize("test_case", load_test_data())
def test_input_validation(test_case):
    field = test_case["field"]
    raw_input = test_case["input"]
    expected = test_case["expected"]

    # Type conversion logic (VERY IMPORTANT)
    if raw_input == "None":
        input_value = None
    elif raw_input.isdigit():
        input_value = int(raw_input)
    else:
        input_value = raw_input

    if field == "username":
        result = validate_username(input_value)

    elif field == "age":
        result = validate_age(input_value)

    elif field == "email":
        result = validate_email(input_value)

    assert result == expected
