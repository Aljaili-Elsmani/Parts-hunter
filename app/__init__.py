from flask import Flask
import sqlite3
import os

DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.secret_key = "your_secret_key"

    # إنشاء قاعدة البيانات والجدول إذا لم يكن موجودًا
    if not os.path.exists(DB_NAME):
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()
        c.execute("""
            CREATE TABLE products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price TEXT NOT NULL,
                category TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()

    # استدعاء جميع الروابط (routes)
    from app import routes
    return app
