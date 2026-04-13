# 2025-ITCS224-UnitTest-6788184

Exercise 4 focused on building and testing simple Python functions with the built-in unittest framework.

## Project Overview

This repository contains:

- A small Python program that classifies a person into a life stage based on age.
- Unit tests for age classification logic.
- Examples of subtests for repeated assertions across multiple input values.

## Life Stage Rules

The function categorize_by_age(age) in age.py returns:

- Child: ages 0 to 9
- Adolescent: ages 10 to 18
- Adult: ages 19 to 65
- Golden age: ages 66 to 150
- Invalid age: any value outside 0 to 150 (for example, -1 or 151)

## Files

- age.py: main implementation and simple CLI input/output flow.
- test_age.py: unit tests for normal, boundary, and invalid age cases.
- test_subtest.py: subtest examples for even/odd number checks.
- test_subtest_age.py: subtest examples across age ranges for each life stage.

## Requirements

- Python 3.x
- No external packages are required (only standard library modules are used).

## Run the Program

Run the age classification script:

```bash
python age.py
```

You will be prompted to enter an integer age, and the program prints the corresponding life stage.

## Run Tests

Run all tests:

```bash
python -m unittest -v
```

Run individual test modules:

```bash
python -m unittest -v test_age.py
python -m unittest -v test_subtest.py
python -m unittest -v test_subtest_age.py
```

## Current Status

The test suite currently passes:

- 14 tests run
- 0 failures
- 0 errors

## Learning Focus

This exercise demonstrates:

- Testing expected outputs with unittest.
- Verifying edge cases and boundaries.
- Using subTest to validate multiple related inputs in one test method.