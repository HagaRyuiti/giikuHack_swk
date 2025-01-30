import sqlite3

def timecreate(savetime, owner_id=1):
    # データベースファイルの名前
    db_name = "room.db"
    
    # データベース接続
    with sqlite3.connect(db_name) as conn:
        cur = conn.cursor()

    # ルームを作成（仮に owner_id を 1 にする）
        cur.execute("INSERT INTO rooms (name, owner_id) VALUES (?, ?)", (savetime,  owner_id))

# データベースのテーブル一覧を取得する
def time_get_tables():
    # データベースファイルの名前
    db_name = "room.db"
    
    # データベース接続
    with sqlite3.connect(db_name) as conn:
        cur = conn.cursor()
        users = cur.execute("""SELECT * FROM users""")
    return users