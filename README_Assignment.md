
# Software Testing Assignment

## 1. Project Overview

This assignment uses the open-source Python Requests project to practice automated unit testing with pytest.

The custom tests currently focus on the `to_native_string()` utility function from `requests.utils`.

## 2. Tools and Technologies

- Python
- pytest
- pytest-xdist
- pytest-order
- CSV test data
- Visual Studio Code
- Git and GitHub

## 3. Environment Setup

Create and activate a virtual environment, then install the project and testing tools.

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -e .
python -m pip install pytest pytest-xdist pytest-order
```

## 4. Run Automated Tests

Run the custom test file:

```powershell
python -m pytest tests/test_my_assignment.py -v
```

Run tests in parallel using two workers:

```powershell
python -m pytest tests/test_my_assignment.py -v -n 2
```

## 5. Parameterized Testing

The custom tests use `pytest.mark.parametrize` to check multiple input values against their expected outputs.

## 6. External Test Data

The file `tests/test_data.csv` contains input values and their expected outputs. The custom test suite reads this CSV file to execute additional test cases.

## 7. Test Ordering and Parallel Execution

The `pytest-order` plugin is used to specify test execution order. The `pytest-xdist` plugin is used to run tests with multiple workers.

## 8. Current Progress

The custom test suite has been executed successfully, including parameterized and CSV-driven tests.

## 9. Remaining Work

- Complete testing for three selected modules.
- Apply and document Equivalence Class Partitioning (ECP) and Boundary Value Analysis (BVA).
- Complete the Excel test-case sheet.
- Record the required setup video.
- Add test configuration and supporting documentation.
- Commit and push all required files to the group repository.
