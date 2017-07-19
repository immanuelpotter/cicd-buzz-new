# cicd-buzz-new

taken from medium.com/bettercode/how-to-build-a-modern-ci-cd-pipeline-5faa01891a5b by Rob van der Leek

## Pipeline for simple python app

### 1) Python application
Created a simple DevOps-related headline generator app.
Each run of the app produces a random sentence. Code is in the "buzz" directory.

### 2) Unit tests
Next unit tests were written, which can be found in the "tests" directory.
Requirements found in requirements.txt installed in virtual environment.

### 3) Pushed to git
.gitignore venv

### 4) Travis CI
added to automate the testing with every commit. 
.travis.yml has config in root of this repo.
can view results of build in travis dashboard.

### 5) Better Code Hub
notifies where quality of code is lacking with each push.
Sign in with github and press "play" on your repo to check quality of code.
[![BCH compliance](https://bettercodehub.com/edge/badge/immanuelpotter/cicd-buzz-new?branch=master)](https://bettercodehub.com/)

### 6) Turn buzz generator into simple web app
Next a Python Flask wrapper needs to be written round the buzz generator to make the program respond to HTTP requests, and output HTML. found in app.py

### 7) Containerise the web application using Docker
Next the Dockerfile was created which uses the Alpine base image, installs Python and pip, and the web app. It also runs the web app whenever the container is launched with the last line.

### 8) Deploy to Docker Hub
This makes it easier to share containers between environments or go back to a previous version. Created a deploy_dockerhub.sh script in a new .travis directory (.travis.yml stays in project root). This script logs in to docker with the environment variables set manually in travis CI. after the login, the docker image is built and deployed to Dockerhub, where it can be accessed directly.

### 9) Deploy to Heroku
Which is a cloud platform for hosting small and scalable web apps. The script added in this step well take the image from Dockerhub and actually deploy it in a live environment. Can be viewed at https://mysterious-cliffs-10427.herokuapp.com/
refresh for fun!
