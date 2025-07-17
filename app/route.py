from flask import render_template, request
from app import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/order', methods=["GET", "POST"])
def order():
    if request.method == "POST":
        name = request.form['name']
        phone = request.form['phone']
        item = request.form['item']
        category = request.form['category']
        details = request.form['details']
        print(f"طلب جديد من {name} - {phone}: {item} ({category}) - {details}")
        return "تم استلام الطلب، سنتواصل معك قريبًا!"
    return render_template("order.html")
