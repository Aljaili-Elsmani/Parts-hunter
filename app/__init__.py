from flask import Flask
import os
import sqlite3

app = Flask(__name__)
app.secret_key = "your_secret_key"

# مسار قاعدة البيانات
DB_NAME = os.path.join(os.path.dirname(__file__), "..", "database.db")

# إنشاء قاعدة البيانات والجدول إذا لم يكن موجودًا
if not os.path.exists(DB_NAME):
    with sqlite3.connect(DB_NAME) as conn:
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

# استدعاء الروتس بعد إنشاء app
from app import routes
