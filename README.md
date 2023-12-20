# uniquedict

`uniquedict` is a Python package that provides a robust solution for removing duplicate dictionaries from a list based on a specified key. It's designed to handle complex data structures, including nested dictionaries and lists, ensuring efficient and accurate deduplication.

## Features

- **Flexible Deduplication**: Remove duplicates based on any specified key within the dictionaries.
- **Complex Data Handling**: Capable of processing nested and complex data structures.
- **High Performance**: Optimized for efficiency, even with large datasets.
- **Unit Tests**: Comprehensive test suite to ensure reliability and correctness.

## Installation

You can easily install `uniquedict` using pip:

```bash
pip install uniquedict
```

## Usage

Here is a basic example of how to use the remove_duplicates function:

```python
from uniquedict.remove_duplicates import remove_duplicates

users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 1, "name": "Alice"}
]

# Remove duplicates based on the 'id' key
unique_users = remove_duplicates(users, "id")
print(unique_users)
```

## Benchmarking

To benchmark the performance of remove_duplicates, run the benchmark module:

```bash
python -m uniquedict.benchmark
```

This will generate a dataset of 1,000 user dictionaries with 300 duplicates and some embedded duplicate fields, and measure the time taken to remove duplicates.

## Running Tests

To run the test suite:

```bash
poetry run pytest
```

## Contributing

Contributions to `uniquedict` are welcome! Please feel free to submit pull requests.

## License

`uniquedict` is MIT licensed, as found in the LICENSE file. The MIT License is a permissive free software license originating at the Massachusetts Institute of Technology (MIT). It allows you to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software with minimal restrictions.
