Installation
=============
After you have extracted the contents of the archive, run:
```bash
$ pip install python-assignment/
```

Execution
=========
Run the stats cli:
```bash
$ stats --since '2016-06-02 10:00:00' --until '2016-06-02 10:10:00' --output-format json
```
You can use the help option to see the available options
```bash
$ stats --help
Usage: stats [OPTIONS]

Options:
  --since TEXT                    [required]
  --until TEXT                    [required]
  --output-format [json|html|tabular]
  --help                          Show this message and exit.
```

Tests
======
To run the tests first install `tox`
```bash
$ pip install tox
```
Then run `tox` at the repo's root directory.
```bash
$ tox
```
You should see the test results, code coverage stats and linting results for the code (flake8)
