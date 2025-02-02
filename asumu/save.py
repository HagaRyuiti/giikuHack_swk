import sqlite3

def timecreate(savetime, username):
    # データベースファイルの名前
    db_name = "room.db"
    
    # データベース接続
    with sqlite3.connect(db_name) as conn:
        cur = conn.cursor()

    # ルームを作成（仮に username を test にする）
        cur.execute("UPDATE users SET time = ? WHERE username = ?", (savetime,  username))

# データベースのテーブル一覧を取得する
def time_get_tables(username):
    # データベースファイルの名前
    db_name = "room.db"
    
    # データベース接続
    with sqlite3.connect(db_name) as conn:
        cur = conn.cursor()
        users = cur.execute("SELECT time FROM users WHERE username = ?", (username,)).fetchall()
        print(users)
        for time in users:
            Itime = int(time[0])
            Wtime = Itime // 60
            Atime = Itime % 60
    return Wtime , Atime