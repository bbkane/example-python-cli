Fairly recently, it's become possible to write Python packages without a `setup.py`! This is an example of how to do that.

From: https://setuptools.pypa.io/en/latest/userguide/quickstart.html

Create venv and install build tools:

```bash
cd simple-python-package  # this README's directory
python3 -m venv venv
source ./venv/bin/activate
python -m pip install --upgrade setuptools build pip
```

Install symlink locally (make sure the `venv` is still activated so the global python package installation stays clean):

```bash
pip install -e .
 # run entrypoint script to confirm it all works
simple-python-package
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

- Try out ruff
- Get pre-commit working (porbably a separate script here that shells out to run.sh)
- Figure out how to get requirements files working and update dependencies?
- CI/CD?
- Get https://github.com/octodns/octodns-ns1/tree/main/script functionality
- Get VS Code suggested packages (pylance, black, etc.) JSON file