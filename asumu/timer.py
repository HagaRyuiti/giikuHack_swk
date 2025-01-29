from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/timer', methods=['POST'])
def post():
    filed = request.form["field"]
    return render_template('timer.html')


if __name__ == '__main__':
    app.run(debug = True)