from flask import Flask, render_template

app = Flask(__name__)

#ホーム画面
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.htm')

#アカウント画面
@app.route('/account')
def account():
    return render_template('account.htm')

#検索画面
@app.route('/search')
def search():
    return render_template('search.htm')

#作成画面
@app.route('/create')
def create():
    return render_template('create.htm')

#タイム画面
@app.route('/timer')
def timer():
    return render_template('timer.htm')

if __name__ == '__main__':
    app.run(debug = True)