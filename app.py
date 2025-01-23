from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# データベース接続を簡単にするための関数
def get_db_connection():
    conn = sqlite3.connect('news_articles.db')  # SQLite DBファイル
    conn.row_factory = sqlite3.Row  # 行を辞書形式で取得
    return conn

# ルート: ニュース記事一覧
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM news_articles ORDER BY date DESC')  # 最新の記事から表示
    articles = cursor.fetchall()
    conn.close()
    return render_template('index.html', articles=articles)

# ニュース記事追加ページ
@app.route('/add', methods=('GET', 'POST'))
def add_article():
    if request.method == 'POST':
        # フォームからデータを取得
        date = request.form['date']
        subject = request.form['subject']
        content = request.form['content']
        
        # データベースに追加
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO news_articles (date, subject, content) VALUES (?, ?, ?)', 
                       (date, subject, content))
        conn.commit()
        conn.close()

        return redirect(url_for('index'))  # 記事一覧ページにリダイレクト

    return render_template('add.html')  # 記事追加フォーム

# ニュース記事の削除
@app.route('/delete/<int:id>', methods=('POST',))
def delete_article(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM news_articles WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))  # 記事一覧ページにリダイレクト

if __name__ == '__main__':
    app.run(debug=True)
