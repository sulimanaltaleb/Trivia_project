# Trivia_project
 My solutions to Udacity API course "Trivia Project"

## Step 1 
downloaded Starter code for this project from 
https://github.com/sulimanaltaleb/FSND
Then navigate to this directory
/projects/02_trivia_api/starter

## Step 2 Setup the environment
created a virtual env at the starter directory as follows
My project is located at:
/Users/macbookpro/Desktop/Trivia_project
Open Terminal:
cd /Users/macbookpro/Desktop/Trivia_project
virtualenv starter
to activate virtual environment 
source starter/bin/activate
cd starter/frontend
npm install
npm start
This will start the frontend server 
Open another Tab in Terminal by CMD+T
cd /Users/macbookpro/Desktop/Trivia_project/starter/backend
pip install -r requirements.txt
or 
pip3 install -r requirements.txt
dropdb trivia && createdb trivia
psql trivia < trivia.psql
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
