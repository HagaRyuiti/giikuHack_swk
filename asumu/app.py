from flask import Flask, render_template

app = Flask(__name__)

#ホーム画面
@app.route('/')
def home():
    return render_template('home.html')

#

if__name__=='__main__':
    app.run(debug=True)