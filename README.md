# Trivia_project

My solutions to Udacity API course "Trivia Project"

  

## Step 1

I downloaded Starter code for this project from
https://github.com/sulimanaltaleb/FSND
the starter code can be found in this directory:
/projects/02_trivia_api/starter

## Step 2 Setup the environment

 - Create Virtual Environment

> location of project in my local machine:
> > /Users/macbookpro/Desktop/Trivia_project

Open Terminal:

    $ cd /Users/macbookpro/Desktop/Trivia_project

To establiah virtual server, I run this command

    $ virtualenv starter

To activate virtual server, I run this command

    $ source starter/bin/activate

 - Running **frontend** server

    $ cd starter/frontend
    
    $ npm install
    
    $ npm start

   **This will start the frontend server** 

 - Running **backend** server


> Open another Tab in Terminal by CMD+T


    $ cd /Users/macbookpro/Desktop/Trivia_project/starter/backend
    
    $ pip install -r requirements.txt
    
    or
    
    $ pip3 install -r requirements.txt
    
    $ dropdb trivia 
    $ createdb trivia -O suliman
    $ psql trivia < trivia.psql
    
    $ export FLASK_APP=flaskr
    
    $ export FLASK_ENV=development
    
    $ flask run

   **This will start the backend server** 

 ## Step 3 edit models.py

 - Setup the database connection

> database_path = "postgres://{}/{}".format('suliman@localhost:5432',
> database_name)

 ## Step 3 edit "__init __.py" in flaskr folder
 

 - Set up CORS

> 	    CORS(app)

	

 - @TODO: Use the after_request decorator to set Access-Control-Allow

>     @app.after_request
>         def  after_request(response):
>         response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization, true')
>         response.headers.add('Access-Control-Allow-Methods', 'GET, PUT, POST, DELETE, OPTIONS')
>         return response

 1. @TODO: Create an endpoint to handle GET requests for all available categories.
 2. @TODO: Create an endpoint to handle GET requests for questions, including pagination (every 10 questions).
