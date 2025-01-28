from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

#ホーム画面a
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

#アカウント画面
@app.route('/account')
def account():
    return render_template('account.html')

#検索画面
@app.route('/search')
def search():
    return render_template('search.html')

#作成画面
@app.route('/create')
def create():
    return render_template('create.html')

if __name__ == '__main__':
    app.run(debug = True)