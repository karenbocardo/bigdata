# testing in python

https://realpython.com/python-testing/

## Testing Your Code

### Automated vs. Manual Testing

**exploratory testing**: manual  testing, running app and using it
- it is done without a plan, just explore
- to have a set of tests make a list of all the features, inputs and expected results; then go through every item everytime there's a change

### Unit Tests vs. Integration Tests

parts of testing:
- **test step**: what you do
- **test assertion**: checking if what should have happened actually did

types:
- **integration testing**: checks that components operate with each other
  - major challenge: if test fails, it's hard to diagnose the issue without isolating system parts
- **unit test**: smaller test, checks single and small component
  - helps isolate what is broken and fix faster

#### example
checks the output of function against known output

- correct values: `sum()` of numbers `(1,2,3)` equals `6`

```python
assert sum([1, 2, 3]) == 6, "Should be 6"
```

- incorrect result

```python
>>> assert sum([1, 1, 1]) == 6, "Should be 6"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError: Should be 6
```

into a python file called `test_sum.py`

```python
def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

if __name__ == "__main__":
    test_sum()
    print("Everything passed")
```

and in command line run

```shell
$ python test_sum.py
Everything passed
```

### Choosing a Test Runner

#### [`unittesting`](https://docs.python.org/3/library/unittest.html)

- python standard library
- contains both a testing framework and a test runner
- has requirements for writing and executing tests
  1. put tests into classes as methods
  2. use a series of special assertion methods in the unittest.TestCase class instead of the built-in assert statement

how to create a `unittest` case:
1. Import unittest from the standard library
2. Create a class called TestSum that inherits from the TestCase class 
3. Convert the test functions into methods by adding self as the first argument 
4. Change the assertions to use the self.assertEqual() method on the TestCase class 
5. Change the command-line entry point to call unittest.main()

executing [this](builtin_sum/test_unittest.py) file results in
- one success, indicated with `.`
- one failure, indicated with `F`

```shell
$ python test_sum_unittest.py
.F
======================================================================
FAIL: test_sum_tuple (__main__.TestSum)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_sum_unittest.py", line 9, in test_sum_tuple
    self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")
AssertionError: Should be 6

----------------------------------------------------------------------
Ran 2 tests in 0.001s

FAILED (failures=1)
```

#### [`nose`](https://docs.nose2.io/en/latest/)

- compatible with `unittest` tests
- can be used as a drop-in
- to get started, install it and execute it on the command line,
it tries to discover all test scripts named `test*.py` and test cases inheriting from unittest.TestCase in your current directory

```shell
$ pip install nose2
$ python -m nose2
.F
======================================================================
FAIL: test_sum_tuple (__main__.TestSum)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_sum_unittest.py", line 9, in test_sum_tuple
    self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")
AssertionError: Should be 6

----------------------------------------------------------------------
Ran 2 tests in 0.001s

FAILED (failures=1)
```

#### [`pytest`](https://docs.pytest.org/en/latest/)

- supports execution of `unittest` test cases
- `pytest` test cases are a series of functions in a Python file starting with the name `test_`
- support for filtering for test cases
- rerun from the last failing test
- ecosystem of hundreds of plugins
- test case example drops `TestCase`, use of classes and command-line entry point

```python
def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6"
```

## Writing Your First Test

```
project/
│
├── my_sum/
│   └── __init__.py
|
└── test.py
```

> You’ll find that, as you add more and more tests, your single file will become cluttered and hard to maintain, so you can **create a folder called tests/** and split the tests into multiple files
It is convention to ensure **each file starts with test_** so all test runners will assume that Python file contains tests to be executed. Some very large projects split tests into more subdirectories based on their purpose or usage.

### How to Structure a Simple Test

Before you dive into writing tests, you’ll want to first make a couple of decisions:

1. What do you want to test?
2. Are you writing a unit test or an integration test?

Then the structure of a test should loosely follow this workflow:

1. Create your inputs
2. Execute the code being tested, capturing the output
3. Compare the output with an expected result

For this application, you’re testing `sum()`. There are many behaviors in `sum()` you could check, such as:

- Can it sum a list of whole numbers (integers)?
- Can it sum a tuple or set?
- Can it sum a list of floats?
- What happens when you provide it with a bad value, such as a single integer or a string?
- What happens when one of the values is negative?

### How to Write Assertions

**assertion**: writing a test is to validate the output against a known response
- general best practices to write them:
  - make sure tests are repeatable, run test multiple times and make sure it always gives the same result
  - try and assert results that relate to your input data
- methods to assert on values, types and existence of variables

| method                  | equivalent to    |
|-------------------------|------------------|
| .assertEqual(a, b)      | a == b           |
| .assertTrue(x)          | bool(x) is True  |
| .assertFalse(x)         | bool(x) is False |
| .assertIs(a, b)         | a is b           |
| .assertIsNone(x)        | x is None        |
| .assertIn(a, b)         | a in b           |
| .assertIsInstance(a, b) | isinstance(a, b) |

> .assertIs(), .assertIsNone(), .assertIn(), and .assertIsInstance() all have opposite methods, named .assertIsNot(), and so forth.

### Side Effects

- executing a piece of code will alter other things in the environment, such as the attribute of a class, a file on the filesystem, or a value in a database,
these are known as **side effects**; decide if the side effect is being tested before including it in your list of assertions
- if you find that the unit of code you want to test has lots of side effects, you might be breaking the **Single Responsibility Principle**:
the piece of code is doing too many things and would be better off being refactored

## [Executing Your First Test](https://realpython.com/python-testing/#executing-test-runners)

### Executing Test Runners

- test runner
- `unittest` command line
  - `-v` for verbose, lists names of tests it executes with result
  - autodiscovery with `discover`
  - `-s` flag for name of directory
  - `-t` to tell unittest where to execute

## More Advanced Testing Scenarios

the three basic steps of every test:

1. create your inputs
2. execute the code, capturing the output
3. compare the output with an expected result

-  data that you create as an input is known as a **fixture**, create them and reuse them
-  running the same test and passing different values each time and expecting the same result is known as **parameterization**

### Isolating Behaviors in Your Application

techniques you can use to test parts of your application that have many side effects:
- Refactoring code to follow the Single Responsibility Principle
- Mocking out any method or function calls to remove side effects
- Using integration testing instead of unit testing for this piece of the application

### Writing Integration Tests

- is the testing of multiple components of the application to check that they work together
- might require acting like a consumer or user of the application by
  - Calling an HTTP REST API
  - Calling a Python API
  - Calling a web service
  - Running a command line
- most significant difference is that integration tests are checking more components at once and therefore will have **more side effects** than a unit test
- integration tests will require more fixtures to be in place, like a database, a network socket, or a configuration file
- it’s good practice to separate your unit tests and your integration tests (you may only want to run integration tests before you push to production instead of once on every commit);
simple way to separate is with folders

```
project/
│
├── my_app/
│   └── __init__.py
│
└── tests/
    |
    ├── unit/
    |   ├── __init__.py
    |   └── test_sum.py
    |
    └── integration/
        ├── __init__.py
        └── test_integration.py
```

### Testing Data-Driven Applications

- integration tests that require backend data
- these depend on test different fixtures to make sure they are repeatable and predictable
- good technique to use is to store the test data in a folder within your integration testing folder called `fixtures` to indicate that it contains test data,
example:

```
project/
│
├── my_app/
│   └── __init__.py
│
└── tests/
    |
    └── unit/
    |   ├── __init__.py
    |   └── test_sum.py
    |
    └── integration/
        |
        ├── fixtures/
        |   ├── test_basic.json
        |   └── test_complex.json
        |
        ├── __init__.py
        └── test_integration.py
```

- if app depends on data from a remote location, ensure your tests are repeatable
  - it is best practice to store remote fixtures locally


### testing in multiple environments

- (tox)
https://realpython.com/python-testing/#testing-in-multiple-environments

## [Automating the Execution of Your Tests](https://realpython.com/python-testing/#automating-the-execution-of-your-tests) 


## What’s Next

### Introducing Linters Into Your Application

### Keeping Your Test Code Clean

### Testing for Performance Degradation Between Changes

### Testing for Security Flaws in Your Application

# useful links
- simultaneously document and test code with [`doctest`](https://realpython.com/python-doctest/)
- testing python command-line apps [(mocks)](https://realpython.com/python-cli-testing/#mocks)
- [`requests`](https://github.com/getsentry/responses) library complimentary package called `responses` gives you ways to create response fixtures and save them in your test folders