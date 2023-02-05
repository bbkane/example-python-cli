#!/bin/bash

# exit the script on command errors or unset variables
# http://redsymbol.net/articles/unofficial-bash-strict-mode/
set -euo pipefail
IFS=$'\n\t'

# https://stackoverflow.com/a/246128/295807
script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
readonly script_dir

# root is one level above this script
readonly root="${script_dir}/.."

cd "${root}"

# .gitignore assumes this, so let's not make it configurable
readonly venv_name="venv"

# Create venv if necessary
if [ ! -d "${venv_name}" ]; then
    printf "No virtualenv found. Creating...\n\n"
    python3 -m venv venv
    source "${venv_name}/bin/activate"
    python3 -m pip install --editable '.[dev]'
fi

# Activate venv if necessary
# https://docs.python.org/3/library/venv.html#how-venvs-work
# > When a virtual environment has been activated, the VIRTUAL_ENV environment variable is set to the path of the environment. Since explicitly activating a virtual environment is not required to use it, VIRTUAL_ENV cannot be relied upon to determine whether a virtual environment is being used.
# Oh well, still the best tool we got!
# https://stackoverflow.com/a/13864829/2958070
set +u
if [ -z ${VIRTUAL_ENV+x} ]; then
    source "${venv_name}/bin/activate"
fi
set -u

# Shell out to Python now that we're in a root dir and have a venv
# Get actual --help info
python3 ./scripts/run.py "$@"
