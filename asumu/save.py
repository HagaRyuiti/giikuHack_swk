import sqlite3

def timecreate(savetime, username="test"):
    # データベースファイルの名前
    db_name = "room.db"
    
    # データベース接続
    with sqlite3.connect(db_name) as conn:
        cur = conn.cursor()

    # ルームを作成（仮に username を test にする）
        cur.execute("INSERT INTO users (username, time) VALUES (?, ?)", (username,  savetime))

# データベースのテーブル一覧を取得する
def time_get_tables():
    # データベースファイルの名前
    db_name = "room.db"
    
    # データベース接続
    with sqlite3.connect(db_name) as conn:
        cur = conn.cursor()
        users = cur.execute("""SELECT * FROM users""")
    return users
