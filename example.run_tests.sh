#!/bin/bash

# Get the project directory
BASEDIR="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

# Add src to python path
echo "Adding \`src\` directory to the PYTHONPATH.."
export PYTHONPATH="${PYTHONPATH}:${BASEDIR}/src/"

# Set env variables
# TODO remove env variables definition from this file
echo "Set env variables.."
export AZURE_STORAGE_CONNECTION_STRING=""
export AZURE_CONTAINER_NAME=""

# TODO make it recursively find all sub-directories
echo "Running unit tests.."
python3 -m unittest discover tests/blob
