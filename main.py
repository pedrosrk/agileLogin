from flask import Flask, render_template, request, redirect, url_for, session
from api import sentiment as anS
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
        print(session['agree'])
        data['agree'] = session['agree']

        return render_template('profile.html', account=user, infos=data)
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))

@app.route('/satisfaction', methods=['POST'])
def satisfaction():
  # Check if user is loggedin
    if 'loggedin' in session:
      data = anS.sentiment(request.form["message"])
      scores = data.englishSentiment()
      session['text'] = request.form["message"]
      session['score'] = scores
      return render_template('satisfaction.html', pos=scores['pos'], neg=scores['neg'], neu=scores['neu'])
    return redirect(url_for('login'))

@app.route('/home', methods=['POST'])
def back_home():
    if request.form:
      agree = request.form['fav_language']
    else:
      agree = 'NOT_SURE'
    
    session['agree'] = agree
    #insert in dataBase
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')