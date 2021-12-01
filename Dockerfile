FROM python:3.9.6-slim

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True
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

ENV PORT 8000

# Run the web service on container startup.
# Use uvicorn webserver with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
# Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run
# to handle instance scaling.
CMD uvicorn --host 0.0.0.0 main:app --port $PORT
