from flask import Flask, render_template, request, redirect, url_for, session
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = 'agilim'

# Enter your database connection details below
app.config['MYSQL_HOST'] = '54.233.253.102'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'pythonlogin'

# Intialize MySQL
mysql = MySQL(app)

@app.route('/')
def login():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM interations WHERE id = %s', (1,))
    account = cursor.fetchone()
    idx = 5
    username = 'test'
    email = 'test@test.com'
    msg = 'I love you'
    score = {'neg': 0.0, 'neu': 0.192, 'pos': 0.808, 'compound': 0.6369}
    agree = 'NOT_SURE'
    cursor.execute('INSERT INTO interations VALUES (%s, %s, %s, %s, %s, %s)', (idx, username, email, msg, score, agree))
    mysql.connection.commit()
    return account

if __name__ == '__main__':
    app.run(debug=True)