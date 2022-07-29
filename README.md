[![Build Status](https://github.com/ladybug-tools/ladybug-display-schema/workflows/CI/badge.svg)](https://github.com/ladybug-tools/ladybug-display-schema/actions)

[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)

# ladybug-display-schema

Ladybug-display Data-Model Objects

## Installation

```console
pip install ladybug-display-schema
```

## QuickStart

```python
import ladybug_display_schema

```

## API Documentation

[Geometry Schema](https://ladybug-tools.github.io/ladybug-display-schema/geometry.html)

[Display Schema](https://ladybug-tools.github.io/ladybug-display-schema/display.html)

## Local Development

1. Clone this repo locally

```console
git clone git@github.com:ladybug-tools/ladybug-display-schema

# or

git clone https://github.com/ladybug-tools/ladybug-display-schema
```

2. Install dependencies:

```console
cd ladybug-display-schema
pip install -r dev-requirements.txt
pip install -r requirements.txt
```

3. Run Tests:

```console
python -m pytest tests/
```

4. Generate Documentation:

```python
python ./docs.py
```
