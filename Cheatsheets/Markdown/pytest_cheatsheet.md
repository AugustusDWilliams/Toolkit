# PyTest Cheatsheet

## Keyword Expressions

Run all tests with some string ‘validate’ in the name
```bash
pytest -k “validate”
```

Exclude tests with ‘db’ in name but include 'validate'
```bash
pytest -k “validate and not db”
```

---

Run all test files inside a folder demo_tests
```bash
pytest demo_tests/
```

Run a single method test_method of a test class TestClassDemo
```bash
pytest demo_tests/test_example.py::TestClassDemo::test_method
```

Run a single test class named TestClassDemo
```bash
pytest demo_tests/test_example.py::TestClassDemo
```

Run a single test function named test_sum
```bash
pytest demo_tests/test_example.py::test_sum
```

Run tests in verbose mode:
```
pytest -v demo_tests/
```

Run tests including print statements:
```bash
pytest -s demo_tests/
```

Only run tests that failed during the last run
```bash
pytest — lf
```