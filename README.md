![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Azure](https://img.shields.io/badge/Microsoft_Azure-0089D6?style=flat-square&logo=microsoft-azure&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=flat-square&logo=docker&logoColor=white)


# BI - DataObject

The goal of this project is to provide a microservice that allow interaction with Microsoft Azure data objects.

For now, the features to be expected are the creation and deletion of a `blob` or a `container`, and to download and publish a `blob`.


## Table of Contents
1. [Documentation](#documentation)
2. [Setting up dev](#setting-up-dev)
    1. [Requirements](#requirements)
    2. [Clone repository](#clone-repository)
    3. [Virtual environment](#virtual-environment)
    4. [Packages installation](#packages-installation)
    5. [Configuration](#configuration)
    6. [Run unittests](#run-unittests)
3. [Docker](#docker)
    1. [Run](#run)
4. [Branches strategy](#branches-strategy)
5. [Project directory structure](#project-directory-structure)
6. [Contributing](#contributing)
7. [Licence](#licence)


## Documentation

The official documentation can be found [here](https://github.com/CPNV-ES-BI/BI_PYTHON_AZURE/wiki).

## Setting up dev

### Requirements

| Version |  Description  | 
|---|---|
| Python 3.10.7  | For code execution  |
| pip 22.2  | Python package manager  |
| virtualenv 20.16.3  | Python virtual environments tool|
| Docker 20.10.22 | Set of PaaS  |


### Clone repository

```sh
git clone git@github.com:CPNV-ES-BI/BI_PYTHON_AZURE.git
cd BI_PYTHON_AZURE/
git switch develop
```

### Virtual environment

Create a Python virtual environment in `BI_PYTHON_AZURE/` 
```sh
virtualenv --python=python3 env
```

Activate the newly created virtual environment:
```sh
 source env/bin/activate
```
To deactivate an active virtual environment:
```sh
 deactivate
```

### Packages installation

```sh
pip install -r requirements.txt
```

### Configuration 

> Make sure to add the full path to the `src` directory to your `PYTHONPATH`:

1. Rename `.env.variables.sh` to `env.variables.sh`
```sh
mv .env.variables.sh env.variables.sh
``` 
2. Open this file and set your environment variables

3. [Run unittests](#run-unittests) to ensure that the environment is correctly installed.

> If you want to run the project without any `run-*.sh` scripts,
make sure to add the path to the `src` directory to your `PYTHONPATH`.

```sh
export PYTHONPATH="${PYTHONPATH}:/home/example/BI_PYTHON_AZURE/src/"
```

### Run Unittests

#### Run all tests

Execute the shell script `run_unittests.sh`

```sh
./run_unittests.sh
``` 

#### Manually
The framework for running unit tests is [unittests](https://docs.python.org/3.10/library/unittest.html).

> This command will execute any test modules in the root of `tests` directory

```sh
python3 -m unittest discover tests/
```

You can also run a single test this with the following command example:
```sh
python3 tests/test_data_object.py TestDataObject.test_create_object_path_not_exists_object_exists
```

## Docker

### Run

> Not ready yet

1. Activate virtual environment 
```sh
python3 -m venv .venv
source .venv/bin/activate
```

2. Run docker
```sh
docker run python-docker
```

##  Project directory structure

> The `tests` directory must have the same structure as the objects tested in `src`

```sh
├── doc                                   # Documentation directory
│   ├── class_diagram.png
│   └── class_diagram.puml
├── Dockerfile
├── example.run_tests.sh                            
├── LICENSE
├── README.md
├── requirements.txt
├── run_tests.sh
├── src                                   # Project directory
│   ├── app.py
│   ├── blob                              # Blob DataObject directory
│   │   ├── blob_helper.py
│   │   ├── __init__.py
│   ├── config                            # Azure credentials configuration directory
│   │   ├── azure_config.py                       # Where the env variables are retrieved
│   │   ├── client.py                              # Provides the required clients to DataObjects
│   │   └── __init__.py
│   ├── __init__.py
│   ├── interface                         # Where interfaces are defined
│       ├── data_object.py                              
│       └── __init__.py
└── tests                                 # Tests directory
    └── blob
        └── test_blob_helper.py
``` 

## Branches strategy

Refer to the workflow [GitFlow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow).

GitFlow installation:
- [Windows](https://git-scm.com/download/win)
- [Linux/Ubuntu](https://howtoinstall.co/en/git-flow)

Main branches description:

| Branches  | Description |
|---|---|
| main/ | stores the official release history  |
| develop/ | serves as an integration branch for features |
| feature/| fork of `develop/` for a new feature|
|release/|fork of `develop/`, once the release is ready, it should be merge to `main`|


The convention name for `feature/` is `Snake Case`
Example: `feature/my_new_feature`

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/amazing_feature)
3. Commit your Changes (git commit -m 'Add some amazing_feature')
4. Push to the Branch (git push origin feature/amazing_feature)
5. Open a Pull Request

## Licence

Distributed under the MIT License. See LICENSE for more information.