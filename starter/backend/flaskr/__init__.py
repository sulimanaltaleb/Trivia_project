import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category


def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  
  '''
  @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''

  CORS(app)
  '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization, true')
    response.headers.add('Access-Control-Allow-Methods', 'GET, PUT, POST, DELETE, OPTIONS')
    return response
  
  '''
  @TODO: 
  Create an endpoint to handle GET requests 
  for all available categories.
  '''
  @app.route('/categories')
  def get_all_categories():
    selection = Category.query.all()
    categories = {category.id:category.type for category in selection}
    if len(selection) == 0:
      abort(404)
    return jsonify({
      'success' : True,
      'categories' : categories

    })

  '''
  @TODO: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''
  QUESTIONS_PER_PAGE = 10
  def paginate(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page-1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    all_results = [question.format() for question in selection]
    current_result = all_results[start:end]
    return current_result
    
  # Creating endpoint to show all questions
  @app.route('/questions')
  def get_all_questions():
    selection = Question.query.order_by('id').all()
    current_questions = paginate(request,selection)
    categories = Category.query.all()
    category = {category.id:category.type for category in categories}
    if len(current_questions) == 0:
      abort(404)
    return jsonify({
      'success' : True,
      'questions' : current_questions,
      'total_questions' : len(selection),
      'categories' : category
    })


  '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''
  @app.route('/questions/<int:question_id>', methods = ['DELETE'])
  def delete_question(question_id):
    try:
      question = Question.query.filter(Question.id == question_id).one_or_none()
      if question_id is None:
        abort(404)
      question.delete()
      selection = Question.query.order_by('id').all()
      current_questions = paginate(request,selection)
      return jsonify({
        'success' : True,
        'deleted_question' : question_id
      })
    except:
      abort(422)






  '''
  @TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''
  @app.route('/questions', methods = ['POST'])
  def create_question():
    body = request.get_json()
    question = body.get('question', None)
    answer = body.get('answer', None)
    difficulty = body.get('difficulty', None)
    category = body.get('category', None)
    if not question:
      abort(422)
    if not answer:
      abort(422)
    if not difficulty:
      abort(422)
    if not category:
      abort(422)  
    try:
      new_question = Question(question=question,answer=answer,difficulty=difficulty,category=category)
      new_question.insert()
      selection = Question.query.order_by('id').all()
      return jsonify({
        'success' : True,
        'total_questions' : len(selection)
      })
    except:
      abort(422)

   
  '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''
  @app.route('/questions/searchresult', methods=['POST'])
  def get_specific_question():
    body = request.get_json()
    search_term = body.get('searchTerm', None)
    try:
      if search_term:
        selection = Question.query.filter(Question.question.ilike('%{}%'.format(search_term))).all()
        search_result = [question.format() for question in selection]
        return jsonify({
          'success' : True,
          'questions' : search_result,
          'total_questions' : len(selection)
        })
    except:
      abort(422)
  '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''
  @app.route('/categories/<int:category_id>/questions')
  def category_questions(category_id):
    try:
      selection = Question.query.filter(Question.category == str(category_id)).all()
      category_questions = [question.format() for question in selection]
      return jsonify({
        'success' : True,
        'questions' : category_questions,
        'total_questions' : len(selection),
        'category' : category_id
      })
    except:
      abort(404)  


  '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''
  @app.route('/quizzes', methods= ['POST'])
  def quiz():
    try:
      body = request.get_json()
      quiz_category = body.get('quiz_category')
      previous_questions = body.get('previous_questions')
      if(not 'quiz_category' in body and not 'previous_questions' in body):
        abort(422)
      if(quiz_category['id']):
        questions = Question.query.filter_by(category = quiz_category['id']).filter(Question.id.notin_(previous_questions)).all()
      else:
        questions = Question.query.filter(Question.id.notin_(previous_questions)).all()
      if len(questions) > 0:
        generate_question = questions[random.randrange(0,len(questions))].format()
        return jsonify({
          'success' : True,
          'question' : generate_question
        })  
      else:
        return jsonify({
          'success' :True,
          'question' : None
        })
    except:
      abort(422)
  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  
  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      'success' : False,
      'error' : 404,
      'message': 'resource not found'
    }), 404

  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      'success' : False,
      'error' : 422,
      'message': 'unprocessable'
    }), 422

  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
      'success' : False,
      'error' : 400,
      'message': 'bad request'
    }), 400

  return app

    