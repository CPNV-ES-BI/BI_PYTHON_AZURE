#!/bin/bash

# venv activation function
# It does not display the venv but it works
# Check with `which pip` command before and after the execution
activate () {
    source .venv/bin/activate
}

# Get the project directory
BASEDIR="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

# Add `src` to python path
echo "Adding \`src\` directory to the PYTHONPATH.."
export PYTHONPATH="${PYTHONPATH}:${BASEDIR}/src/"

# Copy the env variables file
echo "Create the configuration file if it does not exist.."
cp -n .env.variables.sh env.variables.sh
chmod +x env.variables.sh

# Export the environment variables
export VIRTUAL_ENV_DISABLE_PROMPT=0

# venv Creation
echo "Create the virutal environment.."
python3 -m venv .venv

# venv Activation
echo "Activate the virutal environment.."
chmod +x .venv/bin/activate
activate

# Install dev requirements.txt
echo "Install the requirements to the venv $(which pip)"
pip install -r requirements.txt

echo "Please define your connection string in ./src/env.variables.sh"