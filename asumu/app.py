from flask import Flask, render_template, redirect, url_for, request, jsonify, session
from create import roomcreate
from create import get_tables
from create import roomsearch
from create import login_touroku
from create import createdatabase
from flask_socketio import SocketIO, join_room, leave_room, emit
from save import timecreate
from save import time_get_tables
import sqlite3
import time


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

rooms = {}  # 各ルームごとの参加者リスト

#ログイン画面
@app.route('/')
def login():
    createdatabase()
    return render_template('login.htm')

@app.route('/login', methods=['POST'])
def loginuser():
    data = request.get_json()
    print(f"Received login request: {data}")
    un = data.get('username', )
    pw = data.get('password', )
    print(f"Username: {un}, Password: {pw}")
    user = login_touroku(un, pw)
    print(user)
    
    if user:
        session['username'] = user  # セッションにユーザー名を保存
        return jsonify({'message': 'ユーザーがログインしました'}), 200
    else:
        return jsonify({'message': 'パスワードが異なっています'}), 400

# ホーム画面
@app.route('/home')
def home():
    if 'username' not in session:
        return redirect(url_for('login'))  # ログインしていない場合はログインページへ

    roomlist = get_tables()
    return render_template('home.htm', roomlist=roomlist, username=session['username'])

# ログアウト処理
@app.route('/logout')
def logout():
    session.pop('username', None)  # セッションから削除
    return redirect(url_for('login'))

#アカウント画面
@app.route('/account')
def account():
    username = session['username']
    Mtimelist, Stimelist = time_get_tables(username)
    print(Mtimelist)
    print(Stimelist)
    timelist = {
        'timelist1' : Mtimelist ,
        'timelist2' : Stimelist }
    return render_template('account.htm', timelist=timelist, username=username)

#検索画面
@app.route('/search')
def search():
    roomlist = get_tables()
    print(roomlist)
    return render_template('search.htm', roomlist=roomlist)

#作成画面
@app.route('/create')
def create():
    return render_template('create.htm')

# ルーム画面（入室）
@app.route('/room', methods=['POST'])
def room():
    data = request.get_json()
    roomname = data.get('roomname', '')

    if roomname:
        return jsonify({"status": "success", "roomname": roomname})
    else:
        return jsonify({"status": "error", "message": "部屋名が指定されていません"}), 400
    
#ルーム画面（退室）
@app.route('/outroom')
def outroom():
    roomlist = get_tables()
    print(roomlist)
    return render_template('home.htm', roomlist=roomlist)

# ルーム詳細ページ
@app.route('/room/<roomname>')
def room_detail(roomname):
    return render_template('room.htm', roomname=roomname)

# 部屋検索処理 (POSTメソッド対応)
@app.route('/searchroom', methods=['POST'])
def searchroom():
    data = request.get_json()
    key = data.get('roomname', '')
    sroom = roomsearch(key)
    return jsonify(sroom)  # JSON で返す


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
    
@socketio.on('connect')
def handle_connect():
    print(f'Client connected: {request.sid}')

@socketio.on('disconnect')
def handle_disconnect():
    for room, users in rooms.items():
        if request.sid in users:
            users.pop(request.sid)
            leave_room(room)  # ルームからも削除
            emit('update_users', list(users.values()), room=room)
            break
    print(f'Client disconnected: {request.sid}')

# ルーム参加処理（ユーザー名を取得して送信）
@socketio.on('join_room')
def handle_join(data):
    if 'username' not in session:
        return  # ログインしていない場合は処理しない
    
    username = session['username']
    room = data['room']

    join_room(room)

    # ルームの参加者リストを更新
    if room not in rooms:
        rooms[room] = {}
    rooms[room][request.sid] = username

    emit('update_users', list(rooms[room].values()), room=room)

# ルーム退出処理
@socketio.on('leave_room')
def handle_leave(data):
    if 'username' not in session:
        return

    username = session['username']
    room = data['room']

    leave_room(room)

    # ルームの参加者リストを更新
    if room in rooms and request.sid in rooms[room]:
        del rooms[room][request.sid]
        emit('update_users', list(rooms[room].values()), room=room)




#データべースから勉強時間を取得する
@app.route('/getsave', methods=['GET'])
def getsave():
    
    db_name = "room.db"

    with sqlite3.connect(db_name) as conn:
        cur = conn.cursor()

        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")

        table_exists = cur.fetchone()
        if not table_exists:
            print("users テーブルが存在しません。")
            return []
        madetime = cur.execute("""SELECT time FROM users""").fetchall()
        print(madetime)

    return madetime


@app.route('/createsave', methods=['POST'])
def createsave():
    time = request.get_json()
    savetime = time.get('savetime', '')

    if savetime:
        timecreate(savetime, session['username'])  # ユーザー名を渡す
        return jsonify({'message': '勉強時間が保存されました'}), 200
    else:
        return jsonify({'message': '勉強時間が必要です'}), 400
    


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug = True)