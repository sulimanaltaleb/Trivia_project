# Full Stack API Final Project

## Full Stack Trivia

Udacity is invested in creating bonding experiences for its employees and students. A bunch of team members got the idea to hold trivia on a regular basis and created a  webpage to manage the trivia app and play the game, but their API experience is limited and still needs to be built out. 

That's where I came in! I helped them finish the trivia app so they can start holding trivia and seeing who's the most knowledgeable of the bunch. The application has the following features:

1) Display questions - both:
A. all questions
B. questions by category. 
Questions show the question, category and difficulty rating and can show/hide the answer. 
2) a button to delete a question.
3) Adding new question that requires that they include question and answer text.
4) Searching for questions based on a text query string.
5) Play the quiz game, randomly selecting from either all questions or within a specific category. 

## Tasks implemented to complete this project

There were `TODO` comments throughout project. Start by reading the READMEs in:

1. [`./frontend/`](./frontend/README.md)
2. [`./backend/`](./backend/README.md)

In order to complete this project I followed the instructions in those files in order.

### Backend

The `./backend` directory contains completed Flask and SQLAlchemy server. Most of the work primarily done in app.py to define endpoints and it references models.py for DB and SQLAlchemy setup. 

### Frontend

The `./frontend` directory contains a complete React frontend to consume the data from the Flask server. some endpoints were updated accordingly to match with their counterparts in the backend. Those areas are marked with TODO and can be searched for expediency. 

[View the README.md within ./frontend for more details.](./frontend/README.md)

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