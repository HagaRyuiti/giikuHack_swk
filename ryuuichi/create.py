import sqlite3

def roomcreate(roomname):
    # データベースファイルの名前
    db_name = "room.db"
    
    # データベース接続
    with sqlite3.connect(db_name) as conn:
        cur = conn.cursor()

        # room テーブルが存在しない場合のみ作成
        cur.execute("""
            CREATE TABLE IF NOT EXISTS room(
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                name TEXT
            )
        """)

        # room テーブルに新しいルーム名を挿入
        cur.execute("INSERT INTO room(name) VALUES (?)", (roomname,))

        # 現在のすべてのテーブル名を取得
        cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [t[0] for t in cur.fetchall()]

    # テーブル名のリストを返す
    return tables

# テスト実行
table = roomcreate("test_room")
print(table)
