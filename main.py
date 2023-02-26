from flask import Flask, render_template, request, redirect, url_for, session
from api import sentiment as anS
import json
from datetime import datetime
from os.path import exists
# from api import database as db

app = Flask(__name__)
app.secret_key = "agilim"

@app.route('/')
def about():
  return render_template('about.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  # Check if "name" and "email" POST requests exist (user submitted form)
  if request.method == 'POST' and 'name' in request.form and 'email' in request.form:
      # Create variables for easy access
      username = request.form['name']
      email = request.form['email']
      # Create session data, we can access this data in other routes
      session['loggedin'] = True
      session['id'] = email
      session['username'] = username
      # Redirect to home page
      return redirect(url_for('home'))
  return render_template('index.html')

# This will be the logout page
@app.route('/logout')
def logout():
  # Remove session data, this will log the user out
  session.pop('loggedin', None)
  session.pop('id', None)
  session.pop('username', None)
  # Redirect to login page
  return redirect(url_for('about'))

# This will be the home page, only accessible for loggedin users
@app.route('/home')
def home():
    # Check if user is loggedin
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('home.html', username=session['username'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))

# This will be the profile page, only accessible for loggedin users
@app.route('/profile')
def profile():
    # Check if user is loggedin
    if 'loggedin' in session:
        # Show the profile page with account and info
        user={'name': '', 'email': ''}
        user['name'] = session['username']
        user['email'] = session['id']

        data={'msg': '', 'score': {}, 'agree': ''}
        data['msg'] = session['text']
        data['score'] = session['score']
        data['agree'] = session['agree']

        return render_template('profile.html', account=user, infos=data)
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))

@app.route('/satisfaction/english', methods=['POST'])
def satisfactionEnglish():
  # Check if user is loggedin
    if 'loggedin' in session:
      data = anS.sentiment(request.form["message"])
      scores = data.englishSentiment()
      session['text'] = request.form["message"]
      session['method'] = 'englishSentiment'
      if (scores['compound'] > 0.33):
        session['score'] = 'Positivo'
      elif (scores['compound'] > -0.33):
        session['score'] = 'Neutro'
      else:
        session['score'] = 'Negativo'
      
      return render_template('satisfaction.html', comp=session['score'])
    return redirect(url_for('login'))

@app.route('/satisfaction/cliente', methods=['POST'])
def satisfactionCliente():
  # Check if user is loggedin
  if 'loggedin' in session:
    data = anS.sentiment(request.form["message"])
    score = data.sentimentMultinomialNBModel()
    session['score'] = score
    session['method'] = 'sentimentMultinomialNBModel'
    print(score)
    session['text'] = request.form["message"]
    return render_template('satisfaction.html', comp=score)
  return redirect(url_for('login'))

@app.route('/home', methods=['POST'])
def back_home():
    if request.form:
      agree = request.form['fav_language']
    else:
      agree = 'NOT_SURE'
    
    session['agree'] = agree
    #insert in dataBase
    interation={'datetime': '', 'name': '', 'email': '', 'msg': '', 'score': '', 'agree': '', 'method': ''}
    interation['datetime'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    interation['name'] = session['username']
    interation['email'] = session['id']
    interation['msg'] = session['text']
    interation['score'] = session['score']
    interation['agree'] = session['agree']
    interation['method'] = session['method']
    #print(interation)
    if exists('interations.json'):
      with open('interations.json', 'r') as f:
        data = json.load(f)
        data.append(interation)
        json_object = json.dumps(data, indent=2)
    else:
       with open("interations.json", "w") as outfile:
        data = '[]'
        outfile.write(data)
       with open('interations.json', 'r') as f:
        data = json.load(f)
        data.append(interation)
        json_object = json.dumps(data, indent=2)
    
    with open("interations.json", "w") as outfile:
      outfile.write(json_object)
    
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')