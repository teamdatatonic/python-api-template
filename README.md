# Python FastAPI Application Template

Example Python [FastAPI](https://fastapi.tiangolo.com/) application to use as a template. 

Can be productionised on any compute that allows containers.

## Quick Start
### Pre-Requisites:
- [Pyenv](https://github.com/pyenv/pyenv)
- [Poetry](https://python-poetry.org/)
- [Docker](https://www.docker.com/)

Click "Open in Cloud Shell" for a tutorial on how to get started with FastAPI  
[![Open in Cloud Shell](https://gstatic.com/cloudssh/images/open-btn.svg)](https://ssh.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https://github.com/teamdatatonic/python-api-template)

Once in the cloud shell, run the command: `teachme tutorial.md` if it doesn't automatically open. 


### Setup Your Python Environment
```
# Sets up the python virtual environment and installs all required packages
pyenv install
poetry install

# Run unit tests
poetry run pytest --cov

# Run API on http://localhost:5000
poetry run uvicorn --host 0.0.0.0 main:app --port 5000
```

## Develpment best practices
### [Semantic Release](https://github.com/semantic-release/semantic-release)
To enable semantic release on your repository, create a [Personal Access Token](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html) and add it to your project CI variables as `GITLAB_TOKEN`.

### [Commitizen](https://github.com/commitizen/cz-cli)
Auto formats commit messages. This hooks into semantic release and creates major/minor releases depending on the change.

### [Container Vulnerability Scanning](https://cloud.google.com/binary-authorization/docs/creating-attestations-kritis)
The `cloudbuild/container_build.yml` and `policy.yaml` configs build the docker container, analyse it for vulnerabilities and only push the container to the registry if there are no vulnerabilities above a certain policy threshold in `policy.yaml`.  
The "Open in Cloud Shell" tutorial shows you to quickly set this up and adjust to your use case. 