# techniques to test CLI apps

> [cheat sheet](python-testing-techniques.pdf)

the main thing to keep in mind is that you’re just comparing the outputs your code generates to the outputs you expect. everything follows from that.

everything will be structured around a basic Python CLI app that passes data in the form of a multi-level dictionary to two functions that transform it in some way, then prints it to the user.

example code does not include basic best practices for simplicity's sake, can be found [here](testapp.py), and will be tested with the four techniques:

1. [“Lo-Fi” Debugging With Print](#lo-fi-debugging-with-print)
2. [Using a Debugger](#using-a-debugger)
3. [Unit Testing with Pytest and Mocks](#unit-testing-with-pytest-and-mocks)
4. [Integration Testing](#integration-testing)

# “Lo-Fi” Debugging With Print

> [code with print testing](testapp-print.py)

- simplest way to test
- `print` a variable or object that you’re interested in:
  - before a function call: to verify a function’s input
  - after a function call or: to verify a function’s output
  - within a function: to verify a function’s logic

## steps for example

1. see and error when running: there is a missing key

```python
Traceback (most recent call last):
  File "testapp.py", line 60, in <module>
    print_person(final_transformed)
  File "testapp.py", line 23, in print_person
    parents = "and".join(person_data['parents'])
KeyError: 'parents'
```

2. check input to `print_person` and see why our expected output (a printed message) isn’t being generated, adding `print` function before calling it; it shows in its output that we don’t have the top-level parents key—nor the siblings key (*`pprint` to see the object better)

```
final_transformed = final_transform(initial_transformed)
print(final_transformed)
print_person(final_transformed)
```

3. compare output with expected; then see what is going on in `initial_transform`
   - we can also print **markers** to see which logic branches are executed and when
   - internal dictionaries are handled by inner for loop
   - after running, console output hasn’t changed: our `if` statement isn’t working as expected

```python
def initial_transform(data):
    """
    Flatten nested dicts
    """
    for item in list(data):
        if type(item) is dict:
            print "item is dict!"
            pprint(item)
            for key in item:
                data[key] = item[key]

    return data
```

  
## when to use print debugging:

- simple objects
- shorter scripts
- seemingly simple bugs
- quick inspections

## dive deeper:

- [pprint](https://docs.python.org/3/library/pprint.html) - prettify printed objects, prints multi-level objects in a more readable manner

## pros:

- rapid testing
- easy to use

## cons:

- most cases you have to run the whole program, otherwise:
- you need to add extra code to manually control flow
- you can accidentally leave test code when done, especially in complex code

# Using a Debugger

- great for when you want to step through the code one line at a time and inspect the entire application state
- help when you know roughly where errors are happening but can’t figure out why
- give you a nice top-down view of everything happening inside your application at once

## how to use debuggers

> [code with debugger testing](tes)

**breakpoints** are markers on your code that tell your debugger where to pause execution for you to inspect your application state
- added where you want to start or continue a debugging session
- execution will pause on that line and you’ll be able to see variables and their types at that particular point in the program’s execution
- options to navigate code, the most common:
  - *step over*: (one you’ll use most often) simply jumps to the next line of code
  - *step in*: attempts to go deeper into the code, use this when you come across a function call you want to investigate more deeply
  - *step out*: brings us back out to the caller after stepping in

**watches** are expressions that you can add during a debugging session to watch the value of a variable (and more) and are persisted through your app’s execution

> computers do **exactly** what we tell them, after all

## when to use a python debugger:

- more complex projects
- difficult to detect bugs
- you need to inspect more than one object
- you have a rough idea of *where* an error is occurring, but need to zero in on it

## dive deeper:

- conditional breakpoints
- evaluating expressions while debugging

## pros:

- control over flow of program
- bird’s-eye view of application state
- no need to know exactly where the bug is occurring

## cons:

- difficult to manually watch very large objects
- long-running code will take very long to debug

# Unit Testing with Pytest and Mocks

- unit tests to test an application in a more structured, detailed, and automated way
- is a testing technique that breaks down source code into recognizable units (usually methods or functions) and tests them individually
- **code coverage**: you write a script or group of scripts that test each method with different inputs to ensure every logic branch within each method is tested (** aim for 100% code coverage)
- each test treats the method being tested in isolation
  - **mocking**: technique to give reliable return values and any object set up before the test is removed after the test, done to assure the independence and isolation of the unit under test
- **repeatability** and **isolation** are key to these kinds of tests

## pytest

> see test practice folder [here](pytest/)

test writes a unit test for `initial_transform` to show how to set up a set of expected inputs and outputs and make sure they match up
1. set up a fixture that will take some parameters and use those to generate the test inputs and expected outputs that I want
   -  think about the test cases that you will need in order to hit all possible branches

```python
import pytest
import testapp as app

@pytest.fixture(params=['nodict', 'dict'])
def generate_initial_transform_parameters(request):
```

2. build inputs and expected outputs
   
```python
@pytest.fixture(params=['nodict', 'dict'])
def generate_initial_transform_parameters(request):
    test_input = {
        'name': 'John Q. Public',
        'street': '123 Main St.',
        'city': 'Anytown',
        'state': 'FL',
        'zip': 99999,
    }
    expected_output = {
        'name': 'John Q. Public',
        'street': '123 Main St.',
        'city': 'Anytown',
        'state': 'FL',
        'zip': 99999,
    }

    if request.param == 'dict':
        test_input['relastionships'] = {
            'siblings': ['Michael R. Public', 'Suzy Q. Public'],
            'parents': ['John Q. Public Sr.', 'Mary S. Public'],
        }
        expected_output['siblings'] = ['Michael R. Public', 'Suzy Q. Public']
        expected_output['parents'] = ['John Q. Public Sr.', 'Mary S. Public']

    return test_input, expected_output
```

3. write the test, passing the fixture to the test function as a parameter to have access to it
   - test functions should be prepended with test_ and should be based on [assert statements](https://realpython.com/python-assert-statement/): asserts that  the output we get from passing our input to our real function is equal to our expected output

```python
def test_initial_transform(generate_initial_transform_parameters):
    test_input = generate_initial_transform_parameters[0]
    expected_output = generate_initial_transform_parameters[1]
    assert app.initial_transform(test_input) == expected_output
```

4. run the test, either:
   - in IDE with test configuration or
   - with `pytest` in the CLI

```shell
$ pytest python-basics/testing/techniques
```
shell output:

```shell
(venv) ➜  src git:(main) ✗ pytest python-basics/testing/techniques
============================== test session starts ==============================
platform darwin -- Python 3.11.0, pytest-7.2.0, pluggy-1.0.0
rootdir: /Volumes/GoogleDrive/My Drive/internship/src
collected 0 items / 1 error                                                     

==================================== ERRORS =====================================
_______ ERROR collecting python-basics/testing/techniques/test_testapp.py _______
python-basics/testing/techniques/test_testapp.py:2: in <module>
    import testapp as app
python-basics/testing/techniques/testapp.py:100: in <module>
    print_person(final_transformed)
python-basics/testing/techniques/testapp.py:58: in print_person
    parents = "and".join(person_data['parents'])
E   KeyError: 'parents'
============================ short test summary info ============================
ERROR python-basics/testing/techniques/test_testapp.py - KeyError: 'parents'
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.29s ================================
```

5. solve problem

```python
def initial_transform(data):
    """
    Flatten nested dicts
    """
    for item in list(data):
        if type(data[item]) is dict:
            for key in data[item]:
                data[key] = data[item][key]
            data.pop(item)

    return data
```

shell output:

```shell
(venv) ➜  src git:(main) ✗ pytest python-basics/testing/techniques
=========================== test session starts ===========================
platform darwin -- Python 3.11.0, pytest-7.2.0, pluggy-1.0.0
rootdir: /Volumes/GoogleDrive/My Drive/internship/src
collected 2 items                                                         

python-basics/testing/techniques/test_testapp-pytest.py ..          [100%]

============================ 2 passed in 0.09s ===========================
```

## mocks

> see test practice folder [here](mock/)

- we are only testing a single unit of code, we don’t really care about what other function calls do
  - want to have a reliable return from them

### example
outside function call:

```python
def initial_transform(data):
    """
    Flatten nested dicts
    """
    for item in list(data):
        if type(data[item]) is dict:
            for key in data[item]:
                data[key] = data[item][key]
            data.pop(item)

    outside_module.do_something()
    return data
```

don’t want to make live calls to `do_something()`, instead, make a **mock** in test script
- mock will catch this call and return whatever you set the mock to return
- it is very powerful
- can be set up in fixtures, since it's a part of test setup to keep setup code together
- the `do_something` call will be intercepted and return 1
- take advantage of **fixture parameters** to determine what your **mock returns** (important when a code branch is determined by the result of the outside call)

```python
@pytest.fixture(params=['nodict', 'dict'])
def generate_initial_transform_parameters(request, mocker):
    [...]
    mocker.patch.object(outside_module, 'do_something')
    mocker.do_something.return_value(1)
    [...]
```

- `side_effect` allows you to mock different returns for successive calls to the same function
  - set up with a list of outputs (for each successive call) passed to `side_effect`:

testapp

```python
data.pop(item)

    outside_module.do_something()
    outside_module.do_something()
    return data
```

test_testapp
```python
@pytest.fixture(params=['nodict', 'dict'])
def generate_initial_transform_parameters(request, mocker):
    [...]
    mocker.patch.object(outside_module, 'do_something')
    mocker.do_something.side_effect([1, 2])
    [...]
```

## wrapup

### when to use python unit testing frameworks:

- large, complex projects
- oss projects

### helpful tools:

- [pytest fixtures](https://docs.pytest.org/en/latest/fixture.html)
- [deepdiff](https://pypi.python.org/pypi/deepdiff) for comparing complex objects
- mocker

### pros:

- automates running tests
- can catch many types of bugs
- simple setup and modification for teams

### cons:

- tedious to write
- has to be updated with most code changes
- won’t replicate true application running

# [Integration Testing](https://realpython.com/python-cli-testing/#wrapup_3)

# useful links

- run [pytest](https://docs.pytest.org/en/7.1.x/how-to/usage.html)
- [visual studio test configuration](https://code.visualstudio.com/docs/python/testing)
- [how to unit test Flask applications with the minimum viable test suite](https://realpython.com/the-minimum-viable-test-suite/)
- [set up mock servers to test third-party APIs](https://realpython.com/testing-third-party-apis-with-mock-servers/)