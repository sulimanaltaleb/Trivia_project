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
 ```
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "success": true
}
```
 2. @TODO: Create an endpoint to handle GET requests for questions, including pagination (every 10 questions).
 ```
 {
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "questions": [
    {
      "answer": "Maya Angelou", 
      "category": 4, 
      "difficulty": 2, 
      "id": 5, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": 5, 
      "difficulty": 3, 
      "id": 6, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }, 
    {
      "answer": "Muhammad Ali", 
      "category": 4, 
      "difficulty": 1, 
      "id": 9, 
      "question": "What boxer's original name is Cassius Clay?"
    }, 
    {
      "answer": "Brazil", 
      "category": 6, 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": 6, 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "George Washington Carver", 
      "category": 4, 
      "difficulty": 2, 
      "id": 12, 
      "question": "Who invented Peanut Butter?"
    }, 
    {
      "answer": "Lake Victoria", 
      "category": 3, 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": 3, 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }, 
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }, 
    {
      "answer": "Escher", 
      "category": 2, 
      "difficulty": 1, 
      "id": 16, 
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    }
  ], 
  "success": true, 
  "total_questions": 20
}
```
 3. @TODO: Create an endpoint to DELETE question using a question ID.
 ```
{
    'success': True,
    'deleted_question':question_id
}
```
 4. @TODO: Create an endpoint to POST a new question.
 ```
{
    'success': True,
    'total_questions':len(selection)
}
```
 5. @TODO: Create a POST endpoint to get questions based on a search term.
 ```
{
  "questions": [
    {
      "answer": "Muhammad Ali", 
      "category": 4, 
      "difficulty": 1, 
      "id": 9, 
      "question": "What boxer's original name is Cassius Clay?"
    }
  ], 
  "success": true, 
  "total_questions": 1
}

```
 6. @TODO: Create a GET endpoint to get questions based on category.

```
 {
  "category": 1, 
  "questions": [
    {
      "answer": "The Liver", 
      "category": 1, 
      "difficulty": 4, 
      "id": 20, 
      "question": "What is the heaviest organ in the human body?"
    }, 
    {
      "answer": "Alexander Fleming", 
      "category": 1, 
      "difficulty": 3, 
      "id": 21, 
      "question": "Who discovered penicillin?"
    }, 
    {
      "answer": "Blood", 
      "category": 1, 
      "difficulty": 4, 
      "id": 22, 
      "question": "Hematology is a branch of medicine involving the study of what?"
    }, 
    {
      "answer": "Suliman Altaleb", 
      "category": 1, 
      "difficulty": 1, 
      "id": 24, 
      "question": "who is Suliman altaleb?"
    }, 
    {
      "answer": "Python", 
      "category": 1, 
      "difficulty": 5, 
      "id": 26, 
      "question": "This Coding program"
    }
  ], 
  "success": true, 
  "total_questions": 5
}
```
 7. @TODO: Create a POST endpoint to get questions to play the quiz.
 ```
{
  "question": 
    {
      "answer": "Python", 
      "category": 1, 
      "difficulty": 5, 
      "id": 26, 
      "question": "This Coding program"
    }, 
  "success": true
}
```
 8. @TODO: Create error handlers for all expected errors including 404 and 422.
 > http://127.0.0.1:5000/questions?page=599
 ```
 {
  "error": 404, 
  "message": "resource not found", 
  "success": false
}
```

## Testing
To run the tests, on the Terminal "backend" directory, RUN:
>     $ dropdb trivia_test
>     $ createdb trivia_test -O suliman
>     $ psql trivia_test < trivia.psql
>     python test_flaskr.py
```
macbookpro@MacBooks-MacBook-Pro backend % python test_flaskr.py
..............
----------------------------------------------------------------------
Ran 14 tests in 0.497s

OK
```

