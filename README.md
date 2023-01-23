![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Azure](https://img.shields.io/badge/Microsoft_Azure-0089D6?style=flat-square&logo=microsoft-azure&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=flat-square&logo=docker&logoColor=white)


# BI - DataObject

The goal of this project is to provide a microservice that allow interaction with Microsoft Azure data objects.
The microservice will have its own API that will allow interaction with its Data Object library.


## Table of Contents
1. [Documentation](#documentation)
2. [Setting up dev](#setting-up-dev)
    1. [Requirements](#requirements)
    2. [Clone repository](#clone-repository)
    3. [Configuration of the development environment](#configuration-of-the-development-environment)
       1. [Linux terminal environment](#linux-terminal-environment)
       2. [Manual configuration (Linux/Windows)](#manual-configuration--linuxwindows-)
   4. [Run unittests](#run-unittests)
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

### Configuration of the development environment

The development environment requires the following:
- Add the `src` directory to the PYTHONPATH
- Assign the environment variable `AZURE_STORAGE_CONNECTION_STRING`
- Installing the library prerequisites in `requirements.txt`

#### Linux terminal environment

It is possible to configure its environment via the script `setting_up_env.sh` But its purpose will be to prepare the production environment.
The library contained in `src` will be functional, but you will still have to configure your IDE with the points mentioned in the introduction of this section. 

```shell
source setting_up_env.sh
``` 

Then just set your connection string in `env.variables.sh`.

#### Manual configuration (Linux/Windows)

For the configuration of the IDE please refer to the Wiki.

##### Create the Virtual environment

Create a Python virtual environment in `BI_PYTHON_AZURE/` 
```sh
python3 -m venv venv
```

Activate the newly created virtual environment:
For windows refer to the [official documentation](https://docs.python.org/3/library/venv.html#how-venvs-work)
```sh
source .venv/bin/activate
```

To deactivate an active virtual environment:
```sh
 deactivate
```

##### Install the requirements

```sh
pip install -r requirements.txt
```

##### Set your connection string

On Windows you have to create a new environment variable named `AZURE_STORAGE_CONNECTION_STRING`.
You can refer to this [documentation](https://www.roelpeters.be/set-environment-variables-in-virtual-environment-python/).

For linux rename `.env.variables.sh` to `env.variables.sh`
In command line 
```sh
cp .env.variables.sh env.variables.sh
``` 

Then perform the following command to add this to your virtual environment.
```sh
source env.variables.sh
```

### Run Unittests

> Make sure to be at the root level of the project when you run these commands.

#### Run all tests
> 
```shell
python3 -m unittest discover
```

It is possible on Linux to launch all unit tests via the script  `run_tests.sh`

```sh
./run_unittests.sh
``` 

#### Run one test
The framework for running unit tests is [unittests](https://docs.python.org/3.10/library/unittest.html).

> This command will execute any test modules in the root of `tests` directory

```sh
python3 -m unittest discover tests/
```

You can also run a single test this with the following command example:
```sh
python3 tests/test_my_class.py TestMyClass.test_create_object_path_not_exists_object_exists
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
├── doc                                     # Documentation directory
│   ├── interface_class_diagram.png
│   └── interface_class_diagram.puml
├── Dockerfile                              # DockerFile
├── env.variables.sh                        # Where is defined the value of AZURE_STORAGE_CONNECTION_STRING env
├── LICENSE     
├── README.md
├── requirements.txt                        # Contains the required external python modules 
├── run_tests.sh                            # Run tests script
├── setting_up_env.sh                       # Script for the production environnment
│
├── src                                     # Library src directory
│   ├── app.py
│   ├── blob                                # Contains the blob_helper module
│   │   ├── blob_helper.py                  
│   │   ├── errors                              # Contains blob_helper custom exception classes
│   │   ├── __init__.py
│   ├── config                              # Configuration module
│   │   ├── azure_client.py                     # This class provides required Azure Client
│   │   ├── azure_config.py                     # This class get the local variable environment
│   │   ├── __init__.py
│   ├── container                           # Contains the container_helper module
│   │   ├── container_helper.py                 
│   │   ├── errors                              # Contains container_helper custom exception classes
│   │   ├── __init__.py
│   ├── __init__.py
│   └─── interface
│       ├── data_object.py
│       ├── errors
│       └─── __init__.py
│  
├── tests                                   # Unittests test directory
│   ├── blob
│   │   ├── files                          
│   │   ├── __init__.py
│   │   └── test_blob_helper.py
│   ├── container
│   │   ├── __init__.py
│   │   └── test_container_helper.py
│   └─── __init__.py

``` 

## Contributing

> Refer to our [branches strategy](https://github.com/CPNV-ES-BI/BI_PYTHON_AZURE/wiki#branches-strategy) and this [convention names](https://github.com/CPNV-ES-BI/BI_PYTHON_AZURE/wiki#convention-names)

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/amazing_feature)
3. Commit your Changes (git commit -m 'Add some amazing_feature')
4. Push to the Branch (git push origin feature/amazing_feature)
5. Open a Pull Request

## Licence

Distributed under the MIT License. See LICENSE for more information.