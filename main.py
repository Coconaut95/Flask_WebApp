# Python web app with Flask and Google App Engine (web hosting)
# Setting Google Cloud SDK 
# source: https://realpython.com/python-web-applications/

# About requirements.txt: Google App Engine will use this file to install the
# necessary python dependencies for your project when setting it up on the server.

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Congrats!, it's a web app!!</h1>"

# To run the script locally
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)

# Deploy the python web app: two parts ---> On Google Cloud Platform and Locally

## Set up on Google App Engine:  * New Project on Google Cloud Platform. 
##                               * Project-ID: flaskwebapp-360514
##                               * Google App Engine dashboard

## Set up locally for deployment: * Open terminal prompt
##                                * change directory to the project folder
##                                * run: gcloud app deploy (it'll show a error)
##                                * gcloud auth login
##                                * run: gcloud config set project <PROJECT_ID> 
##                                * to confirm: gcloud projects list
##                                * run: gcloud app deploy
##                                * confirm region (16 para sudamerica)
##                                * confirm Deploy
##                                * Va a tirar error porque hay que habilitar una API específica y para ello hay que meter datos de la tarjeta de crédito. 

## Continuarlo con la cuenta personal y no la laboral