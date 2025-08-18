# ML-deployment-UV-FastAPI

# UV and FastAPI Webservice libraries for ML Deployment

* Note: I'll use GitHub Codespaces for this workshop. It can be done locally.

* Create a new repo on GitHub, on that repository, create a codespace. Turn the codespace to a visual studio code format.

* run docker, python -V --> to test your codespace for the packages

* pip install jupyter scikit-learn pandas numpy

* Notebook for this workshop [workshop-uv-fastapi.ipynb](workshop-uv-fastapi.ipynb)

* jupyter nbconvert --to script workshop-uv-fastapi.ipynb  --> convert the notebook to python script.
Note: 
- clean the workshop-uv-fastapi.py into train.py and predict_old.py scripts
- the train.py script can be orchestrated with Airflow or Prefect etc.

* run python3 [train.py](train.py), [predict_old.py](predict_old.py) --> u should get an output from both scripts

## WEBSERVICE WITH FASTAPI AND UVICORN

* pip install fastapi uvicorn

* run python3 [ping.py](ping.py) --> to test the FastAPI. Add /ping to the url to get PONG (http://127.0.0.1:9696/ping)

* http://127.0.0.1:9696/docs  --> open the docs of fastapi that's running. click try it out, click execute

* python3 [predict.py](predict.py) --> http://127.0.0.1:9696/docs, click try it out, click execute.

* uvicorn predict:app --host 0.0.0.0 --port 9696 --reload --> run this instead to avoid running predict.py all times when there's an update

* python3 [test.py](test.py) --> run in a new terminal and ensure to keep the flask app running


## Using UV to avoid dependency conflict 

* UV is alot faster than pipenv, poetry, venv requirements.txt. UV is written in Rust

* pip install uv

* uv init --> initialize uv project. you should see pyproject.toml, main.py

* Edit the pyproject.toml by changing this line from <description = "Add your description here"> to <description = "Churn Service">

* uv add scikit-learn fastapi uvicorn --> add libraries. check created uv.lock for added packages and pyproject.toml for added dependencies

* uv add --dev requests --> add dev dependency not for production. check updated pyproject.toml file for added dependency. Also check for created .venv folder

* uv run uvicorn predict:app --host 0.0.0.0 --port 9696 --reload  --> always add 'uv run' to any script

* uv run python3 [test.py](test.py)


## Put all in DOCKER for Production

* create a [dockerfile](Dockerfile) --> check the codes

* docker build -t churn_prediction . --> run to build the image

* docker run -it --rm -p 9696:9696 churn_prediction --> run the docker container

### Deployment: The docker container can be deployed as Kubernetes job or any cloud platform. Here fly.io was used for deployment

* curl -L https://fly.io/install.sh | sh --> install fly.io

* nano ~/.bashrc --> Manually add the directory to your $HOME/.bash_profile (or similar)
  export FLYCTL_INSTALL="/home/codespace/.fly"
  export PATH="$FLYCTL_INSTALL/bin:$PATH"

* which fly --> run this in a new terminal to see path of installed fly.io (/home/codespace/.fly/bin/fly)

* fly auth signup --> authenticate fly to create an account. Watch out for payment.

* fly launch --generate-name --> did not finish this because of payment



# Deployment with RUNPOD