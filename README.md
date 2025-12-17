# API AutoTests Framework

An automated testing framework for API testing based on web app https://github.com/Nikita-Filonov/qa-automation-engineer-api-course. The framework uses Pytest with various plugins for comprehensive test coverage and reporting.

## Features

- **API Testing**: Comprehensive testing suite for REST APIs
- **Multiple Domains**: Covers users, courses, exercises, authentication, and file operations
- **Allure Reporting**: Detailed test reports with Allure
- **Pydantic Configuration**: Type-safe configuration management
- **Flexible Test Execution**: Parallel test execution and custom markers
- **Code Coverage**: Swagger API coverage tracking

## Project Structure

```
autotests-api/
├── clients/               # API client implementations
├── fixtures/              # Pytest fixtures
├── tests/                 # Test suites organized by domain
├── testdata/              # Test data and files
├── tools/                 # Utility modules and helpers
├── config.py              # Application configuration
├── conftest.py            # Pytest configuration
├── pytest.ini             # Pytest settings
├── requirements.txt       # Dependencies
└── .env                   # Environment variables
```

## Prerequisites
- Installed Python 3.10 + 
- Setup and run app https://github.com/Nikita-Filonov/qa-automation-engineer-api-course

## Setup

1. Clone the repository
   ```bash
   git clone https://github.com/GETrofimov/autotests-api.git
   ```
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
3. Activate virtual environment:
   - Windows: `.venv\Scripts\activate`
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Configure environment variables in `.env` file

## Available Test Markers

The framework uses custom Pytest markers for test categorization:

- `@pytest.mark.users`: Tests related to user management
- `@pytest.mark.regression`: Regression tests
- `@pytest.mark.authentication`: Authentication-related tests
- `@pytest.mark.files`: File handling tests
- `@pytest.mark.courses`: Course management tests
- `@pytest.mark.exercises`: Exercise-related tests

## Running Tests

### Basic Test Run

```bash
pytest
```

### Run Tests with Specific Marker

```bash
pytest -m users  # Run only user-related tests
pytest -m "authentication and regression"  # Run authentication regression tests
```

### Generate Allure Report

```bash
# Run tests with Allure
pytest --alluredir=./allure-results

# Generate and serve HTML report
allure serve ./allure-results
```

## Dependencies

Key dependencies include:
- `pytest`: Test framework
- `allure-pytest`: Reporting framework
- `httpx`: HTTP client
- `pydantic`: Data validation and settings management
- `Faker`: Test data generation
- `swagger-coverage-tool`: API coverage tracking

For complete list, see `requirements.txt`