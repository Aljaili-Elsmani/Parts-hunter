from flask import Flask

# إنشاء تطبيق Flask
app = Flask(__name__)

# استيراد الروابط بعد تعريف app
from app import routes
