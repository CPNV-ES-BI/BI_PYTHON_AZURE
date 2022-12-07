![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Azure](https://img.shields.io/badge/Microsoft_Azure-0089D6?style=flat-square&logo=microsoft-azure&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=flat-square&logo=docker&logoColor=white)


# BI - DataObject

## Table of Contents
1. [Documentation](#documentation)
2. [Setting up dev](#setting-up-dev)
    1. [About my development environment](#about-my-development-environment)
    2. [Requirements](#requirements)
    3. [Clone repository](#clone-repository)
    4. [Configuration](#configuration)
    5. [Run unittests](#run-unittests)
3. [Docker](#docker)
    1. [Run](#run)
4. [Contributing](#contributing)

## Documentation

The official documentation can be found [here](https://github.com/CPNV-ES-BI/BI_PYTHON_AZURE/wiki).

## Setting up dev

### About my development environment

- Ubuntu
- Visual Studio Code
    - IntelliSense Python extension (Microsoft)

### Requirements

- Python3.8 or higher       (For code execution)
- Docker version 20.10.X    (To run Docker)

### Clone repository

```sh
git clone git@github.com:CPNV-ES-BI/BI_PYTHON_AZURE.git
cd BI_PYTHON_AZURE/
git checkout develop
```

### Configuration 

> Make sure to add the full path to the `src` directory to your `PYTHONPATH`:

```sh
export PYTHONPATH="${PYTHONPATH}:/home/example/BI_PYTHON_AZURE/src/"
```

### Run Unittests

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

#### Run all tests

Execute the shell script `run_unittests.sh`

```sh
./run_unittests.sh
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

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/AmazingFeature)
3. Commit your Changes (git commit -m 'Add some AmazingFeature')
4. Push to the Branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

## Licence

Distributed under the MIT License. See LICENSE for more information.