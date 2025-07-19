from flask import Flask

app = Flask(__name__)

# استيراد المسارات
from app import routes
