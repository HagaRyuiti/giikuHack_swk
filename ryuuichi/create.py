import sqlite3

def roomcreate(roomname ):
    #roomの作成、アクセス
    room = (roomname + ".db")
    conn = sqlite3.connect(room)
    #sqliteを操作するカーソルオブジェクトの生成
    cur = conn.cursor()

    #roomテーブルの作成
    cur.execute("CREATE TABLE room(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)")

    #SQL文の実行
    conn.commit()

    sql = "SELECT name FROM sqlite_master WHERE TYPE='table'"

    for t in cur.execute(sql):
        tables = t

    #データベースにコミット
    conn.close()

    return tables


table = roomcreate("test")

print(table)
