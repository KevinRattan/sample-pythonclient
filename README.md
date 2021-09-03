# This is a very simple python client.

# Several changes are needed for you to use it against the events API:

1. Three k8s variables need to be provided:
    URL - the url of the backend service
    PORT - the port the application should run on
    DEBUG - False so that it will run in production mode

# You should create the Dockerfile that:

1. Uses a Python3 base image
1. Installs all the necessary dependencies
1. Runs the flask application inside gunicorn

