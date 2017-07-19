# cicd-buzz-new

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
