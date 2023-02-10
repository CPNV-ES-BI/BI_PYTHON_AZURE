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
   3. [Configuration](#configuration)
   4. [Run the project](#run-the-project)
   5. [Run the unit tests](#run-the-unit-tests)
3. [Docker](#docker)
   1. [Docker requirements](#docker-requirements)
   2. [Docker compose](#docker-compose)
   3. [Production](#production)
   4. [Docker (manual)](#docker--manual-)
4. [Project directory structure](#project-directory-structure)
5. [Contributing](#contributing)
   1. [Pipeline](#pipeline)
6. [License](#licence)


## Documentation

- The official documentation can be found [here](https://github.com/CPNV-ES-BI/BI_PYTHON_AZURE/wiki).
- The list of issues can be found [here](https://github.com/CPNV-ES-BI/BI_PYTHON_AZURE/wiki/Issues).

## Setting up dev

### Requirements

| Version |  Description  | 
|---|---|
| Python 3.10.7  | For code execution  |
| pip 22.2  | Python package manager  |
| virtualenv 20.16.3  | Python virtual environments tool|
 

### Clone repository

```sh
git clone git@github.com:CPNV-ES-BI/BI_PYTHON_AZURE.git
cd BI_PYTHON_AZURE/
git switch develop
```

### Configuration

The development environment requires to:
- Create the virtual environment
- Add the `src` directory to the PYTHONPATH
- Assign the environment variable
- Installing the library prerequisites in `requirements.txt`

> If you use the PyCharm IDE refer to this documentation and go to point 3 [here](https://github.com/CPNV-ES-BI/BI_PYTHON_AZURE/wiki/1-BI_PYTHON_AZURE-Project#configure-pycharm).

1. Activate virtual environment 
```sh
python3 -m venv .venv
source .venv/bin/activate
```

2. Add src to the `PYTHONPATH`
```shell
export PYTHONPATH="$PYTHONPATH:src"
```

2. Copy `example.settings.env` and name it `secret.settings.env`
```shell
cp -n example.settings.env secret.settings.env
```

4. Now set the environment variables
> Currently, the project module only refer to `AZURE_STORAGE_CONNECTION_STRING`

- `AZURE_STORAGE_CONNECTION_STRING`: is the Azure connection string
- `REGION`: is the Azure environment which refers to a specific location where the service is deployed.
- `CONTAINER`: is the main container on which the microservice will interact

5. Install the requirements of this project (external Python packages) 
```shell
pip install -r requirements.txt 
```

### Run the project
> At the moment the main Framework is not installed. It will be Flask RESTful.
> It is possible to launch the flask project which should display "Hello World!
```shell
python3 -m flask run --host=0.0.0.0
```

### Run the unit tests
> Make sure to launch them at the root of the project.

Run all tests with this following command. The `-v` is for verbosity.
It will retrieve all the tests in the project.
```shell
python3 -m unittest discover -v
```

Run a single test with the `-k`. It will run all the tests that match the specified pattern.
> For now, if tests have the same name, they will both be run by this command.
> 
> The correct syntax to run one test with the Framework Unittest is:
> `python -m unittest my_module.TestMyClass.test_my_function`
> but for the moment it is not functional
```shell
python3 -m unittest discover -k test_delete_object_object_containing_sub_objects_exists_object_deleted_recursively -v
```

## Docker

> You can refer to the [Docker Wiki documentation](https://github.com/CPNV-ES-BI/BI_PYTHON_AZURE/wiki/4-Docker).

The current project has 3 different containers implemented in the `Dockerfile`.
- bi_python_azure:production reachable by the service `production`. It directly run the flask server.
- bi_python_azure:development  reachable by the service `development`. By default it run the flask server but it is possible to run unit tests.
- bi_python_azure:tests  reachable by the service `tests`. It directly run all tests.

### Docker requirements

| Version                                                             |  Description  | 
|---------------------------------------------------------------------|---|
| [Docker 23.0.0](https://docs.docker.com/engine/install/ubuntu/)     | Set of PaaS   |
| [Docker Compose V2](https://docs.docker.com/compose/install/linux/) | tool for deploying Docker containers  |


### Docker compose
> Make sure to execute these command from the root directory of this project

1. Build a service (it could be `production`, `development` or `tests`)
```shell
docker compose build development
```
2. Start the service

```shell
docker compose up development
```
Or use `-d` argument to run the service in the background. this will launch the service in the background.
```shell
docker compose up development -d
```

3. Execute any tests command
> The production service **CANNOT** run tests.
> 
> Please refer to this [section](#run-the-unit-tests) about tests commands outputs
Run all tests
```shell
docker compose exec development python3 -m unittest discover -v
```
Run a single test
```shell
docker compose exec development python3 -m unittest discover -k test_delete_object_object_containing_sub_objects_exists_object_deleted_recursively -v
```

4. Stop service
Stop all services
```shell
docker compose stop
```
Stop one services
```shell
docker compose stop development
```

### Production
> When the Framework Rest will be implemented, it is with the published production container that we will interact.
> For now here is how to launch the production image

```shell
docker compose build production
docker compose up production
```

### Docker (manual)

This section allows you to launch docker containers without using the Docker compose tool.
Here is an example with `tests` container. It will directly execute all unit tests.

1. Build
```shell
docker build . --tag bi_python_azure --file Dockerfile --target tests
```
2. Run
```shell
docker run --env-file secret.settings.env bi_python_azure-tests:latest
```

##  Project directory structure

> The `tests` directory must have the same structure as the objects tested in `src`


```sh
BI_PYTHON_AZURE                                 
├── act.secret.env
├── doc                                     # Documentation, contains diagrams images and .puml
│   ├── full_class_diagram.png
│   ├── full_class_diagram.puml
│   ├── interface_class_diagram.png
│   └── interface_class_diagram.puml
├── docker-compose.yml                      # Docker Compose configuration file 
├── Dockerfile                              # Script to automate the creation of Docker images, container..
├── example.settings.env                    # Example configuration file for secrets.
├── LICENSE                                     
├── README.md
├── requirements.txt
├── src                                     # Project src directory
│   ├── app.py                              # Flask Framework entrypoint
│   ├── blob                                # Blob sub package
│   │   ├── blob_helper.py                    # BlobHelper module, allows to interact with azure blob objects
│   │   ├── errors                            # Custom exceptions related to BlobHelper
│   │   └── __init__.py
│   ├── config                              # Configuration sub package
│   │   ├── azure_client.py                 # AzureClient module: provides Azure clients, depends on AzureConfig module
│   │   ├── azure_config.py                 # AzureConfig module: get the local variable environment
│   │   └── __init__.py
│   ├── container                           # Container sub package
│   │   ├── container_helper.py               # ContainerHelper module, allows to interact with azure container objects
│   │   ├── errors                            # Custom exceptions related to ContainerHelper
│   │   └── __init__.py
│   ├── __init__.py
│   └── interface                           #  Contains Interface definition
│       ├── data_object.py                    # "interface" implemented by BlobHelper and ContainerHelper modules
│       ├── errors                            # Contains the top parent exception for DataObject
│       └── __init__.py 
└── tests                                   # Project tests directory
    ├── blob
    │   ├── files                             # Contains the files used in the test class. 
    │   ├── __init__.py
    │   └── test_blob_helper.py               # TestBlobHelper module
    ├── container   
    │   ├── __init__.py
    │   └── test_container_helper.py          # TestContainerHelper module
    └── __init__.py
``` 

## Contributing

> Refer to the [branch strategy](https://github.com/CPNV-ES-BI/BI_PYTHON_AZURE/wiki/1-BI_PYTHON_AZURE-Project#branches-strategy) and the [convention name](https://github.com/CPNV-ES-BI/BI_PYTHON_AZURE/wiki/1-BI_PYTHON_AZURE-Project#convention-names).
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/amazing_feature)
3. Commit your Changes (git commit -m 'Add some amazing_feature')
4. Push to the Branch (git push origin feature/amazing_feature)
5. Open a Pull Request

> If the changes in your branch involve the use of external python packages, please update the requirements:
> `pip3 freeze > requirements.txt`
> 
> If these packages are specific to the development environment, please create a new one:
> `pip3 freeze > requirements_dev.txt`

### Pipeline

During push and pull requests, a pipeline CI has been set up via GitHub actions. It is only when the tests passed with success that these operations are possible.

Please refer to [pipeline wiki documentation](https://github.com/CPNV-ES-BI/BI_PYTHON_AZURE/wiki/5-Pipeline)

## Licence

Distributed under the MIT License. See LICENSE for more information.