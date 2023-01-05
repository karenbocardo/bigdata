# [errors](https://docs.python.org/3/tutorial/errors.html)

two types of errors:
1. [syntax errors](#syntax-errors)
2. [exceptions](#exceptions)

# syntax errors

- the most common kind of complaint you get while you are still learning
- parser repeats the offending line and displays a little ‘arrow’ pointing at the earliest point in the line where the 
error was detected

# exceptions

- detected during execution are called exceptions and are not unconditionally fatal
- most exceptions are not handled by programs, however, and result in error messages,
 last line of the error message indicates what happened
- exceptions come in different **types**, and the type is printed as part of the message
- rest of the line provides detail

## handling exceptions

> see: [built-in exceptions](https://docs.python.org/3/library/exceptions.html#built-in-exceptions)

```python
while True:
...     try:
...         x = int(input("Please enter a number: "))
...         break
...     except ValueError:
...         print("Oops!  That was no valid number.  Try again...")
...
```

`try` statement work flow:
  1. try clause is executed
  2. `except` clause skipped if no exception occurs
  3. if exception occurs during execution of `try`, rest is skipped,
`except` clause is executed and execution continues after
  4. if exception occurs and does not math exception named in `except`
clause, is passed on to outer `try` statements; if no handler found, is is _unhandled exception_ and execution stops

### exception's arguments

- presence and types of the arguments depend on the exception type

```python
try:
...     raise Exception('spam', 'eggs')
... except Exception as inst:
...     print(type(inst))    # the exception instance
...     print(inst.args)     # arguments stored in .args
...     print(inst)          # __str__ allows args to be printed directly,
...                          # but may be overridden in exception subclasses
...     x, y = inst.args     # unpack args
...     print('x =', x)
...     print('y =', y)
...
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs
```

### exception types

- `BaseException`: common base class of all exceptions
  - subclass `Exception`: base class of all the non-fatal exceptions,
can be used as a wildcard that catches (almost) everything
>  it is good practice to be as specific as possible with the types of exceptions that we intend to handle, and to allow any unexpected exceptions to propagate on

### handling

print or log the exception and then re-raise it (allowing a caller to handle the exception as well)

```python
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise
```

### `else` clause

it is optional; when present, must follow all except _clauses_.
useful for code that must be executed if the _try clause_ does not raise an exception

```python
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
```

## raising exceptions

allows the programmer to force a specified exception to occur,
indicates the exception to be raised

## exception chaining

if an unhandled exception occurs inside an except section, it will have the exception being handled attached to it and included in the error message:

```python
try:
...     open("database.sqlite")
... except OSError:
...     raise RuntimeError("unable to handle error")
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'database.sqlite'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError: unable to handle error
```

to indicate that an exception is a direct consequence of another, the raise statement allows an optional from clause:

```python
# exc must be exception instance or None.
raise RuntimeError from exc
```

## user-defined exceptions

- programs may name their own exceptions by creating a new exception class
- should typically be derived from the `Exception` class
- defined with names that end in “Error”

## clean up actions

### defining

 optional _clause_ which is intended to define clean-up actions that must be executed under all circumstances

```python
try:
...     raise KeyboardInterrupt
... finally:
...     print('Goodbye, world!')
...
Goodbye, world!
KeyboardInterrupt
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
```

`finally` clause executes as the last task before `try` statement completes.
it returns whether or not the try statement produces an exception. it is executed in any event.

> it is useful for releasing external resources (such as files or network connections), regardless of whether the use of the resource was successful.

when an exception occurs:
1. during `try` it may be handled by `except`, if not, the exception is re-raised after `finally` is executed
2. also re-raises when it occurs during `else`
3. executes `break`, `continue` or `return`
   - exceptions are not re-raised when `finally` executes any
   - if `try` reaches a statement, `finally` executes prior to the statement execution
4. if `finally` includes `return`, returned value is from the `finally` clause and not the `try`

### predefined

- some objects define standard clean-up actions to be undertaken when the object is no longer needed, regardless of whether or not the operation using the object succeeded or failed
- objects which provide predefined clean-up actions will indicate this in their documentation

## raising and handling multiple unrelated exceptions

(situations where it is necessary to report several exceptions that have occurred)

### [exception groups](https://docs.python.org/3/library/exceptions.html#exception-groups)

- `ExceptionGroup` wraps a list of exception instances so that they can be raised together
- it is an exception itself, so it can be caught like any other exception

```python
def f():
...     excs = [OSError('error 1'), SystemError('error 2')]
...     raise ExceptionGroup('there were problems', excs)
...
>>> f()
  + Exception Group Traceback (most recent call last):
  |   File "<stdin>", line 1, in <module>
  |   File "<stdin>", line 3, in f
  | ExceptionGroup: there were problems
  +-+---------------- 1 ----------------
    | OSError: error 1
    +---------------- 2 ----------------
    | SystemError: error 2
    +------------------------------------
>>> try:
...     f()
... except Exception as e:
...     print(f'caught {type(e)}: e')
...
caught <class 'ExceptionGroup'>: e
>>>
```

-  `except*` to selectively handle only the exceptions in the group that match a certain type

```python
def f():
...     raise ExceptionGroup("group1",
...                          [OSError(1),
...                           SystemError(2),
...                           ExceptionGroup("group2",
...                                          [OSError(3), RecursionError(4)])])
...
>>> try:
...     f()
... except* OSError as e:
...     print("There were OSErrors")
... except* SystemError as e:
...     print("There were SystemErrors")
...
There were OSErrors
There were SystemErrors
  + Exception Group Traceback (most recent call last):
  |   File "<stdin>", line 2, in <module>
  |   File "<stdin>", line 2, in f
  | ExceptionGroup: group1
  +-+---------------- 1 ----------------
    | ExceptionGroup: group2
    +-+---------------- 1 ----------------
      | RecursionError: 4
      +------------------------------------
>>>
```

-  exceptions nested in an exception group must be instances, not types

## enriching exceptions with notes

- when an exception is created in order to be raised, it is usually initialized with information that describes the error that has occurred
- exceptions have a method `add_note(note)` that accepts a string and adds it to the exception’s notes list
- traceback rendering includes all notes, in the order they were added, after the exception

```python
try:
...     raise TypeError('bad type')
... except Exception as e:
...     e.add_note('Add some information')
...     e.add_note('Add some more information')
...     raise
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: bad type
Add some information
Add some more information
>>>
```