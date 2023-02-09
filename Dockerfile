ARG BUILD_IMAGE=python:3.10.9-slim-buster
ARG USER_NAME=bi_az
ARG APP_WORKDIR=app

# Build
#-----------
FROM ${BUILD_IMAGE} AS build

ARG USER_NAME
ARG APP_WORKDIR

#RUN apt-get update && apt-get upgrade -y
WORKDIR /$APP_WORKDIR
# Sets utf-8 encoding for Python
ENV LANG=C.UTF-8
# Tells Python not to buffer the console output.
ENV PYTHONUNBUFFERED=1
# Create a user and its group
RUN groupadd -g 513 $USER_NAME
RUN useradd -g $USER_NAME -m -u 42065 $USER_NAME
# Ensures that the python and pip executables used will be those from our virtualenv.
ENV PATH="/venv/bin:$PATH"
# Setup the virtualenv
RUN python -m venv /venv
# Install requirements
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
# Copy project src directory
COPY src src
# Add src directory to PYTHONPATH to ease the command execution
ENV PYTHONPATH "${PYTHONPATH}:src"
# Expose port
EXPOSE 5000
# Make USER_NAME and its group owner of APP_WORKDIR
RUN chown -R $USER_NAME:$USER_NAME /$APP_WORKDIR

# Production
#-----------
FROM build AS production
USER $USER_NAME
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]

# Development
#-----------
FROM production AS development
# Disables Python from writing bytecode files in order to reflect code changes without manual deletion of bytecode files
ENV PYTHONDONTWRITEBYTECODE=1
# Copy test directory
COPY tests tests
USER $USER_NAME
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]

FROM development AS tests
USER $USER_NAME
CMD [ "python3", "-m" , "unittest", "discover", "-v"]

