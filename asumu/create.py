import sqlite3

def createdatabase():
    db_name = "room.db"

    with sqlite3.connect(db_name) as conn:
        cur = conn.cursor()

        # users テーブルを作成
        cur.execute(""" 
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                time TEXT,
                password TEXT
            );
        """)

        # rooms テーブルを作成
        cur.execute(""" 
            CREATE TABLE IF NOT EXISTS rooms (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
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

        conn.commit()

def roomcreate(roomname, owner_id=1):
    db_name = "room.db"
    
    with sqlite3.connect(db_name) as conn:
        cur = conn.cursor()

        # ルームを作成
        cur.execute("INSERT INTO rooms (name, owner_id) VALUES (?, ?)", (roomname, owner_id))

        # 作成したルームにオーナー（owner_id）をメンバーとして追加
        room_id = cur.lastrowid  # 新しく作成したルームのIDを取得
        cur.execute("INSERT INTO room_members (user_id, room_id) VALUES (?, ?)", (owner_id, room_id))

        conn.commit()

def login_touroku(username, password):
    db_name = "room.db"

    with sqlite3.connect(db_name) as conn:
        cur = conn.cursor()

        # `users` テーブルの存在確認
        cur.execute("SELECT * FROM users WHERE username = ?", (username,))
        existing_user = cur.fetchone()

        if existing_user:
            stored_password = existing_user[3]
            if stored_password == password:
                return username  # 認証成功
            else:
                return False  # パスワードが一致しない
        else:
            # ユーザーが存在しない場合、新規登録
            try:
                cur.execute(
                    "INSERT INTO users (username, time, password) VALUES (?, ?, ?)",
                    (username, "0", password)
                )

                conn.commit()  # 変更を保存
                return username  # 新規登録成功
            except sqlite3.IntegrityError:
                return False  # 重複エラー


# データベースのroomsテーブル一覧を取得する関数
def get_tables():
    db_name = "room.db"
    
    with sqlite3.connect(db_name) as conn:
        cur = conn.cursor()
        
        # rooms テーブルが存在するかをチェック
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='rooms'")
        table_exists = cur.fetchone()

        if not table_exists:
            print("rooms テーブルが存在しません。")
            return []

        # rooms テーブルが存在すれば一覧を取得
        rooms = cur.execute("SELECT name FROM rooms").fetchall()

    print(rooms)
    
    return [{"name": room[0]} for room in rooms]

# データベースのroomsテーブルを検索して取得する関数
def roomsearch(key):
    db_name = "room.db"
    
    with sqlite3.connect(db_name) as conn:
        cur = conn.cursor()
        
        # rooms テーブルが存在するかをチェック
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='rooms'")
        table_exists = cur.fetchone()

        if not table_exists:
            print("rooms テーブルが存在しません。")
            return []

        # 部分一致検索
        search_key = f"%{key}%"  # '%' を key に付与して部分一致検索
        searchrooms = cur.execute(
            "SELECT name FROM rooms WHERE name LIKE ?", (search_key,)
        ).fetchall()

    print(searchrooms)
    
    return [{"name": searchroom[0]} for searchroom in searchrooms]
