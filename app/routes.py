from flask import render_template, request
from app import app

# الصفحة الرئيسية
@app.route('/')
def home():
    return render_template("index.html")

# صفحة "عن الموقع"
@app.route('/about')
def about():
    return render_template("about.html")

# صفحة "تواصل معنا"
@app.route('/contact')
def contact():
    return render_template("contact.html")

# صفحة "طلب قطع غيار"
@app.route('/order', methods=["GET", "POST"])
def order():
    if request.method == "POST":
        name = request.form['name']
        phone = request.form['phone']
        item = request.form['item']
        category = request.form['category']
        details = request.form['details']
        
        # مؤقتًا نطبع الطلب في اللوج (يمكن تطويره لاحقًا)
        print(f"طلب جديد من {name} - {phone}: {item} ({category}) - {details}")
        return "تم استلام الطلب، سنتواصل معك قريبًا!"
    
    return render_template("order.html")
