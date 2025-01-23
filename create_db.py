import sqlite3

def create_table():
    conn = sqlite3.connect('news_articles.db')  # データベース接続
    cursor = conn.cursor()

    # テーブル作成のSQL
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS news_articles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        subject TEXT NOT NULL,
        content TEXT NOT NULL
    )
    ''')

    conn.commit()  # 変更を確定
    conn.close()   # 接続を閉じる

if __name__ == '__main__':
    create_table()  # テーブル作成
    print("Database and table created successfully.")
