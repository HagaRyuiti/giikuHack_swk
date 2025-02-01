import sqlite3

def roomcreate(roomname, owner_id=1):
    # データベースファイルの名前
    db_name = "room.db"
    
    # データベース接続
    with sqlite3.connect(db_name) as conn:
        cur = conn.cursor()

        # users テーブルを作成
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                subject TEXT UNIQUE NOT NULL,
                time TEXT  NOT NULL,
                online TEXT UNIQUE NOT NULL
            );
        """)

        # rooms テーブルを作成
        cur.execute("""
            CREATE TABLE IF NOT EXISTS rooms (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                owner_id INTEGER NOT NULL,
                FOREIGN KEY (owner_id) REFERENCES users (id) ON DELETE CASCADE
            );
        """)

        # room_members テーブルを作成
        cur.execute("""
            CREATE TABLE IF NOT EXISTS room_members (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                room_id INTEGER NOT NULL,
                joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE,
                FOREIGN KEY (room_id) REFERENCES rooms (id) ON DELETE CASCADE
            );
        """)

        # ルームを作成（仮に owner_id を 1 にする）
        cur.execute("INSERT INTO rooms (name, owner_id) VALUES (?, ?)", (roomname,  owner_id))


# データベースのroomsテーブル一覧を取得する関数
def get_tables():
    db_name = "room.db"
    
    with sqlite3.connect(db_name) as conn:
        cur = conn.cursor()
        rooms = cur.execute("""SELECT name FROM rooms""").fetchall()

    print(rooms)
    
    return [{"name": room[0]} for room in rooms]

#データベースのroomsテーブルを検索して取得する関数
def roomsearch(key):
    db_name = "room.db"
    
    with sqlite3.connect(db_name) as conn:
        cur = conn.cursor()
        search_key = f"%{key}%"  #'%' を key に付与して部分一致検索
        searchrooms = cur.execute(
            "SELECT name FROM rooms WHERE name LIKE ?", (search_key,)
        ).fetchall()

    print(searchrooms)
    
    return [{"name": searchroom[0]} for searchroom in searchrooms]


