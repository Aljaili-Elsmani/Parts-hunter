from flask import Flask

app = Flask(__name__)

# استيراد المسارات من routes.py
from app import routes
