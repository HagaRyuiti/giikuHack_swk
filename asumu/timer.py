from flask import Flask, render_template, request

app = Flask(__name__)

#タイム画面
@app.route('/homer')
def timer():
    return render_template('home.htm')

if __name__ == '__main__':
    app.run(debug = True)