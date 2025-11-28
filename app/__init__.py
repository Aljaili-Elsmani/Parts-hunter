from flask import Flask
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "your_secret_key"

DB_NAME = "/opt/render/project/src/database.db"

# إنشاء قاعدة البيانات إذا لم تكن موجودة
if not os.path.exists(DB_NAME):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price TEXT NOT NULL,
            category TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

from app import routes
