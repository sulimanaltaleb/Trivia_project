# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Tasks

1. Use Flask-CORS to enable cross-domain requests and set response headers. 

> `    CORS(app)`

2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
METHOD Url
Request parameters
Response body

3. Create an endpoint to handle GET requests for all available categories. 
4. Create an endpoint to DELETE question using a question ID. 
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
6. Create a POST endpoint to get questions based on category. 
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
9. Create error handlers for all expected errors including 400, 404, 422 and 500. 


## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```


# Project Outline 
**1. Get Categories:**
> an endpoint to handle GET requests for all available categories.
> 
METHOD Url :  `GET '/categories' ` 
Request parameters: `None`
Response body: `json of categories, status.`

##### EXAMPLE: 
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
**2. Get Questions:**
> endpoint to handle GET requests for questions, including pagination (every 10 questions)..
> 
METHOD Url :  `GET '/questions?page=(page_number)' ` 
Request parameters: `page=(page_number) or 1 by default`
Response body: `json of categories, questions, status, total_questions.`
##### EXAMPLE: 
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
**3. Delete a Question:**
> endpoint to DELETE question using a question ID.
> 
METHOD Url :  `DELETE '/questions/<int:question_id>'` 
Request parameters: `question_id`
Response body: `json of question_id, status.`
```
{
    'success': True,
    'deleted_question':question_id
}
```
**4. Create new Question:**
> an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score.
> 
METHOD Url :  `POST '/questions' ` 
Request parameters: `[question:string, answer:string, difficulty:int, category:int]`
Response body: `json of total_questions, status.`

##### EXAMPLE: 
``` 
{
    'success': True,
    'total_questions':len(selection)
}
```
**5. Questions Search:**
> endpoint to get questions based on a search term.
> 
METHOD Url :  ` POST '/questions/searchresult'` 
Request parameters: `string:searchTerm`
Response body: `json of questions, status, total_questions.`
##### EXAMPLE: 

-   Post a new search for a specific questions
-   Request Date: SearchTerm:string
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
**6. Questions by Category:**
> endpoint to get questions based on category.
> 
METHOD Url :  `GET '/categories/<int:category_id>/questions'` 
Request parameters: `int:category_id`
Response body: `json of category_id, questions, status, total_questions.`
##### EXAMPLE: 
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
**7. Quiz Questions:**
> endpoint to get questions to play the quiz.
> 
METHOD Url :  ` POST '/quizzes'` 
Request parameters: `quiz_category, previous_questions `
Response body: `json of question, status`
##### EXAMPLE: 
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

**8. Error Handlers:**
> error handlers for all expected errors including 400, 404, 422 and 500.
> 
METHOD Url :  `[http://127.0.0.1:5000/questions?page=599]'` 
Request parameters: `None `
Response body: `json of error, message,status`
##### EXAMPLE: 
```
{
 "error": 404, 
 "message": "resource not found", 
 "success": false
}
```
**9. TESTING:**
To run the tests, on the Terminal "backend" directory, RUN:
```
$ dropdb trivia_test
$ createdb trivia_test -O suliman
$ psql trivia_test < trivia.psql
```
```
$ python test_flaskr.py
..............
----------------------------------------------------------------------
Ran 14 tests in 0.497s

OK
```