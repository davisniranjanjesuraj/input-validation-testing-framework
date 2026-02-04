# Input Validation & Negative Testing Framework

## Project Overview
This project is a **data-driven input validation and negative testing framework** built using **Python and PyTest**.  
It focuses on validating how a system handles **invalid inputs, boundary values, and error messaging**, ensuring robustness and reliability in real-world scenarios.

The framework simulates backend validation logic and systematically tests it using **automated negative test cases**, producing a professional **HTML test report** as the final outcome.

---

##  Objectives
- Validate system behavior against **invalid and edge-case inputs**
- Ensure **clear and correct error messages** are returned
- Apply **data-driven testing** for scalability and maintainability
- Generate **automated test execution reports** for review and submission

---

##  Testing Scope
The framework validates the following input fields:

| Field     | Validation Criteria |
|----------|---------------------|
| Username | Length, data type, alphanumeric constraints |
| Age      | Numeric type, minimum and maximum boundaries |
| Email    | Data type and format validation |

Each validation includes:
- Negative test cases
- Boundary value analysis
- Type validation

---

##  Tech Stack
- **Programming Language:** Python
- **Testing Framework:** PyTest
- **Reporting:** PyTest-HTML
- **Test Design Technique:** Data-Driven Testing (CSV-based)

---

##  How It Works

###  Application Validation Layer
The `validator.py` file simulates real backend input validation by enforcing:
- Data type checks
- Length constraints
- Boundary conditions
- Format validation

Each function returns either:
- `"VALID"` for successful validation
- A **clear error message** for invalid inputs

---

### Data-Driven Testing
All test cases are stored externally in a CSV file:
- Makes tests easy to extend
- Avoids hardcoding values
- Improves maintainability

Example test data:
```csv
field,input,expected
username,ab,Username length must be between 3 and 15
age,17,Age must be between 18 and 60
email,userexample.com,Invalid email format
```
---
### Automated Test Execution

PyTest dynamically:

Reads test data from the CSV file

Maps inputs to the correct validation function

Executes assertions against expected error messages

#### This ensures:

Consistent validation

High test coverage

Reliable negative testing

---

### Test Reporting

After execution, PyTest generates a self-contained HTML report that includes:

Test summary (Passed / Failed)

Execution time

Detailed assertions

Error traces (if any)

### Output location:

`reports/test_report.html`

---

## How to Run the Project
### Step 1: Clone the Repository
`git clone https://github.com/your-username/input-validation-testing-framework.git`
`cd input-validation-testing-framework`

### Step 2: Install Dependencies
`pip install -r requirements.txt`

### Step 3: Execute Tests
`pytest`

### Step 4: View Test Report

#### Open the following file in a browser:

`reports/test_report.html`

### Sample Output

All negative and boundary tests executed

HTML report generated automatically

Clear visibility into validation failures and system behavior

#### This report can be:

Submitted as an academic/project deliverable

Attached to QA documentation

Showcased in a professional portfolio

---

### Use Case & Industry Relevance

This framework is applicable to:

Web application form validation

Backend API input testing

Regression testing of validation logic

Improving user experience by preventing invalid data entry

---

### Future Enhancements

API-based input validation testing

Integration with CI/CD pipelines (GitHub Actions)

Logging and exception tracking

Parameterization using JSON/YAML

Test coverage metrics

---

### Author
Davis Niranjan

---

### License

This project is intended for educational and portfolio purposes.

