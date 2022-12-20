#!/bin/bash

# Get the project directory
BASEDIR="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

echo "Adding \`src\` directory to the PYTHONPATH.."
export PYTHONPATH="${PYTHONPATH}:${BASEDIR}/src/"

# TODO make it recursively find all sub-directories
echo "Running unit tests.."
python3 -m unittest discover tests/blob
