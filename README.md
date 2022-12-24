Fairly recently, it's become possible to write Python packages with a `setup.py`! This is an example of how to do that.

From: https://setuptools.pypa.io/en/latest/userguide/quickstart.html

Create venv and install build tools:

```bash
cd simple-python-package  # this README's directory
python3 -m venv venv
source ./venv/bin/activate
python -m pip install --upgrade setuptools build pip
```

Install symlink locally (make sure the `venv` is still activated so the global namespace stays clean):

```bash
pip install -e .
 # run entrypoint script to confirm it all works
simple-python-package
```

