#!/bin/bash

# Get the project directory
BASEDIR="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

# Add `src` to python path
echo "Adding \`src\` directory to the PYTHONPATH.."
export PYTHONPATH="${PYTHONPATH}:${BASEDIR}/src/"

# Set env variables
echo "Set env variables.."
source env.variables.sh

# Run any tests in `tests` directory
echo "Running unit tests.."
python3 -m unittest discover -s tests/blob
