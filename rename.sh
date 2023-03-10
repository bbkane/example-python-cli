#!/bin/bash



# exit the script on command errors or unset variables
# http://redsymbol.net/articles/unofficial-bash-strict-mode/
set -euo pipefail
IFS=$'\n\t'

readonly new_project_name="$1"  # thing installed from pip. Can have dashes

readonly new_root_package_name="$2" # thing you import. no dashes

# https://stackoverflow.com/a/246128/295807
script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
readonly script_dir
cd "${script_dir}"

git clean -xdf

find . -type f -not -path '*/\.git\/*' -not -path '\./rename.sh' -print0 \
    | xargs -0 perl -pi -w -e "s/example-python-cli/${new_project_name}/g;"

find . -type f -not -path '*/\.git\/*' -not -path '\./rename.sh' -print0 \
    | xargs -0 perl -pi -w -e "s/example_python_cli/${new_root_package_name}/g;"

mv ./example_python_cli "${new_root_package_name}"

cd ..

mv example-python-cli "${new_project_name}"

printf "Done!\n\n  cd ../%s" "${new_project_name}"
