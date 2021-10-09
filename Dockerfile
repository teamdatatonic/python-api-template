FROM python:3.9-slim

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True
# Run in the defaul standard container port for http services 8080
ENV PORT 8080
# Set the root of the project
ENV APP_HOME /app
WORKDIR $APP_HOME

# Install poetry package manager
RUN pip install poetry

# Copy application dependency manifests to the container image.
# Copying this separately prevents re-running dependency sync on every change.
COPY poetry.lock pyproject.toml $APP_HOME/

# Install production dependencies.
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

# Copy the rest of project files
COPY . $APP_HOME/

# Run the web service on container startup.
# Use gunicorn webserver with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
# Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run
# to handle instance scaling.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
