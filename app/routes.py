from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# بيانات وهمية للمنتجات (يمكنك لاحقاً ربطها بقاعدة بيانات)
products = [
    {
        'name': 'بطارية سيارة',
        'image': 'battery.jpg',
        'whatsapp_message': 'أريد طلب بطارية سيارة'
    },
    {
        'name': 'مبرد مياه',
        'image': 'cooler.jpg',
        'whatsapp_message': 'أريد طلب مبرد مياه'
    }
]

# الصفحة الرئيسية
@app.route('/')
def index():
    return render_template('index.html', products=products)

# صفحة طلب قطعة
@app.route('/order')
def order():
    return render_template('order.html')

# صفحة اتصل بنا
@app.route('/contact')
def contact():
    return render_template('contact.html')

# صفحة حول الموقع
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
