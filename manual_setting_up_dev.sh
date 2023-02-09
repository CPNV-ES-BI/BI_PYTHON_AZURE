#!/bin/bash

# venv activation function
activate () {
    source venv/bin/activate
}

# Get the project directory
BASEDIR="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

# Add `src` to python path
echo "Adding \`src\` directory to the PYTHONPATH.."
export PYTHONPATH="${PYTHONPATH}:${BASEDIR}/src/"

# Copy the env variables file
echo "Create the configuration file if it does not exist.."
# Avoids overwriting the file if it exists
cp -n example.settings.env secret.settings.env
chmod +x secret.settings.env

# venv Creation
echo "Create the virutal environment.."
export VIRTUAL_ENV_DISABLE_PROMPT=0
python3 -m venv venv

# venv Activation
echo "Activate the virutal environment.."
activate

# Install dev requirements.txt
echo "Install the requirements to the venv $(which pip)"
pip install -r requirements.txt

echo "Please define your env variables in secret.settings.env and execute the command:"
echo "source secret.settings.env"