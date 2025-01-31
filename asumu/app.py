from flask import Flask, render_template, redirect, url_for, request, jsonify
from create import roomcreate
from create import get_tables
from save import timecreate
from save import time_get_tables

app = Flask(__name__)

#ホーム画面
@app.route('/')
@app.route('/home')
def home():
    roomlist = get_tables()
    timelist = time_get_tables()
    print(roomlist)
    return render_template('home.htm', roomlist=roomlist, timelist=timelist)


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

# 部屋作成処理 (POSTメソッド対応)
@app.route('/createroom', methods=['POST'])
def createroom():
    data = request.get_json()
    roomname = data.get('roomname', '')
    
    if roomname:
        roomcreate(roomname)  # 部屋を作成
        return jsonify({'message': '部屋が作成されました'}), 200
    else:
        return jsonify({'message': '部屋名が必要です'}), 400

# 勉強時間状況
@app.route('/createsave', methods=['POST'])
def createsave():
    time = request.get_json()
    savetime = time.get('savetime', '')
    
    if savetime:
        timecreate(savetime)  # 部屋を作成
        return jsonify({'message': '勉強時間が保存されました'}), 200
    else:
        return jsonify({'message': '勉強時間が必要です'}), 400

if __name__ == '__main__':
    app.run(debug = True)
