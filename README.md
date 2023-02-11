Fairly recently, it's become possible to write Python packages without a `setup.py`! This is an example of how to do that.

From: https://setuptools.pypa.io/en/latest/userguide/quickstart.html

Create venv and run tests

```bash
cd example-python-cli  # this README's directory
./run.sh test  # setup venv and run tests
```

Activate the venv and run the CLI

```bash
source venv/bin/activate
 # run entrypoint script to confirm it all works
example-python-cli
```

This package can also be installed globally without polluting the global python package installation with [`pipx`](https://pypa.github.io/pipx/)

```bash
pipx install -e .
```

# Notes

## Re-installing Python

This can be necessary when I screw up `scripts/run.sh`.

1. Find location of a package: `python3 -m pip show black`
2. rm the parent folder: `rm -rf /usr/local/lib/python3.10/site-packages`
3. Reinstall Python: `brew reinstall python3`

# TODO

- Try out ruff - blocked on https://github.com/charliermarsh/ruff/issues/282
- Figure out how to get requirements files working and update dependencies?
- CI/CD?
- Get https://github.com/octodns/octodns-ns1/tree/main/script functionality
- test coverage
- I'd like to read TOML using the new stdlib tomlreader lib, but that's only in Python 3.11 and brew hasn't made that default yet - see https://github.com/Homebrew/homebrew-core/pull/114154
