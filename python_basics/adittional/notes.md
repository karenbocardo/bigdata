# notes

> [example code](reader-master)

## virtual environment

create it

```
$ python3 -m venv venv
```

activate it

```
$ source venv/bin/activate
(venv) $
```

install packages

```
(venv) $ python -m pip install <package-name>
```

deactivate

```
(venv) $ deactivate
$
```

## pypi

example package:

```
realpython-reader/
│
├── src/
│   └── reader/
│       ├── __init__.py
│       ├── __main__.py
│       ├── config.toml
│       ├── feed.py
│       └── viewer.py
│
├── tests/
│   ├── test_feed.py
│   └── test_viewer.py
│
├── LICENSE
├── MANIFEST.in
├── README.md
└── pyproject.toml
```

configuration of the reader package:

```toml
# pyproject.toml

[build-system]
requires      = ["setuptools>=61.0.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "realpython-reader"
version = "1.0.0"
description = "Read the latest Real Python tutorials"
readme = "README.md"
authors = [{ name = "Real Python", email = "info@realpython.com" }]
license = { file = "LICENSE" }
classifiers = [
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
]
keywords = ["feed", "reader", "tutorial"]
dependencies = [
    "feedparser >= 5.2.0",
    "html2text",
    'tomli; python_version < "3.11"',
]
requires-python = ">=3.9"

[project.optional-dependencies]
dev = ["black", "bumpver", "isort", "pip-tools", "pytest"]

[project.urls]
Homepage = "https://github.com/realpython/reader"

[project.scripts]
realpython = "reader.__main__:main"
```

# next steps

- [ ] read about python packages and releasing an app
- [ ] see real python articles