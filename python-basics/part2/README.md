# python part 2

> style guide and coding conventions: https://peps.python.org/pep-0008/
> codetags: https://peps.python.org/pep-0350/

## [modules](https://docs.python.org/3/tutorial/modules.html#modules)
A module is a file containing Python definitions and statements. The file name is the module name with the suffix `.py` appended.
Within a module, the module’s name (as a string) is available as the value of the global variable `__name__`.

### example of fibonacci
create a file called `fibo.py` and enter in a file
```python
import fibo
```

if you intend to use a function often you can assign it to a local name:
```python
>>>
>>> fib = fibo.fib
>>> fib(500)
```
other imports:
```python
from fibo import fib, fib2
fib(500)
```
import all [^1]
```python
from fibo import *
fib(500)
```

[^1]: the practice of importing * from a module or package is frowned upon, since it often causes poorly readable code

make the file usable as a script as well as an importable module
```shell
python fibo.py <arguments>
```

```python
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
```

## module search path

1. built-in module names [```sys.builtin_module_names```](https://docs.python.org/3/library/sys.html#sys.builtin_module_names)
2. file in list of directories from:
   
    - directory of input
    - python path
    - installation-dependent default

## "compiled" python files

-  `-o` switch removes assert statements
-  `-oo`switch removes both assert statements and `__doc__` strings (only use this option if you know what you’re doing)
- other notes for experts

## standard modules

`sys`:

- built into every python interpreter
- `sys.ps1` is `>>>`
- `sys.ps2` is `...`
- `sys.path` is a list of string that determines the interpreter's search path for modules

## `dir()` function

used to find out names that a module defines, lists the names you have defined currently (without arguments)

## packages
work within directories
```
sound/                          Top-level package
      __init__.py               Initialize the sound package
      formats/                  Subpackage for file format conversions
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  Subpackage for sound effects
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  Subpackage for filters
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
```
```python
import sound.effects.echo
```

(importing sub-modules might have unwanted side-effects that should only happen when the sub-module is explicitly imported.)

`___all___` list: the list of module names that should be imported when from package `import *` is encountered
```python
__all__ = ["echo", "surround", "reverse"]
```

> there is nothing wrong with using `from package import specific_submodule`! In fact, this is the recommended notation

# input and output

## formatting

ways to format strings:
1. [formatted string literals (f-strings)](#formatted-string-literals-format)
```python
year = 2016
>>> event = 'Referendum'
>>> f'Results of the {year} {event}'
'Results of the 2016 Referendum'
```

2. [`str.format()` method](#strformat-method)
```python
yes_votes = 42_572_654
>>> no_votes = 43_132_495
>>> percentage = yes_votes / (yes_votes + no_votes)
>>> '{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage)
' 42572654 YES votes  49.67%'
```

3. [by using string slicing and concatenation (manual)](#manual)
4. quickly display witb `repr()` (representations that can be read by the interpreter) 
or `str()` (human-readable): many values have the representation in this

### f-strings {#format}

include the value of Python expressions inside a string by prefixing 
the string with `f` or `F` and writing expressions as `{expression}`

[format specifiers](https://docs.python.org/3/library/string.html#formatspec):

- (visit link for complete reference on specifiers)
- `:` after variable
  - decimals, for example: round to three places after decimal `f'The value of pi is approximately {math.pi:.3f}.'`
  - columns lining up with integer after to be a minimum number of characters wide
```python
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
>>> for name, phone in table.items():
...     print(f'{name:10} ==> {phone:10d}')
...
Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678
```
- modifiers
  - `!a` applies `ascii()`
  - `!s` applies `str()`
  - `!r` applies `repr()`
```python
animals = 'eels'
>>> print(f'My hovercraft is full of {animals}.')
My hovercraft is full of eels.
>>> print(f'My hovercraft is full of {animals!r}.')
My hovercraft is full of 'eels'.
```
- `=` specifier yo expand expresseion to text, equal sign and representation
  [(self documenting)](https://docs.python.org/3/whatsnew/3.8.html#bpo-36817-whatsnew)  
```python
bugs = 'roaches'
>>> count = 13
>>> area = 'living room'
>>> print(f'Debugging {bugs=} {count=} {area=}')
Debugging bugs='roaches' count=13 area='living room'
```

### [`str.format()`] method (https://docs.python.org/3/library/string.html#formatstrings)

```python
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
We are the knights who say "Ni!"
```

- number for position
```python
print('{0} and {1}'.format('spam', 'eggs'))
spam and eggs
>>> print('{1} and {0}'.format('spam', 'eggs'))
eggs and spam
```

- keyword arguments
```python
print('This {food} is {adjective}.'.format(
...       food='spam', adjective='absolutely horrible'))
This spam is absolutely horrible.
```

- keyword arguments can be arbitrarily combined
```python
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',
...                                                    other='Georg'))
The story of Bill, Manfred, and Georg.
```

- passing the dict and using square brackets `'[]'` to access the keys
```python
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
...       'Dcab: {0[Dcab]:d}'.format(table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```

### manual
- `str.rjust()`
- `str.ljust()`
- `str.center()`
- `str.zfill()`

# files

- open file with `open(filename, mode, encoding=None)`
  - modes can be `'r'` (which is the default, for only reading),
  `'w'` for writing, `'a'` for appending and `'r+'` for both reading and writing
  - appending a `'b'` to the mode opens file in binary mode
- `with` keyword for file to be properly closed and shorter than `try-finally`...,
if not, use `f.close()` to close file

```python
with open('workfile', encoding="utf-8") as f:
...     read_data = f.read()

>>> # We can check that the file has been automatically closed.
>>> f.closed
True
```
- after a file is closed, attempts to use the object fail

## methods

(examples assume that a file object called `f` has been created)

- `f.read()` (can have the parameter `size`) returns it as a string
- `f.readline()` reads a single line from the file
- loop to read lines `for line in f: print(line, end='')`
- lines in a list `list(f)` or `f.readlines()`
- `f.write(string)` writes string to file
  - other type of objects need to be converted (to a string or bytes, 
  depends on the case)
- `f.tell()` returns integer with file object's current position
- `f.seek(offset, whence)` change file object's position
- `isatty()`, `truncate()`, among others

# saving structured data with [`json`](https://docs.python.org/3/library/json.html#module-json)

**serializing**: standard module called json can take Python data hierarchies, and convert them to string representations

- `dumps()` serializes,`dump()` serializes to a text file
- `load()` to decode

> JSON files must be encoded in UTF-8. Use encoding="utf-8" when opening JSON file as a text file for both of reading and writing.

# [errors](errors.md)