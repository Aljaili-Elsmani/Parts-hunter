from app import app
from flask import render_template

# قائمة المنتجات للمعرض
products = [
    {
        'name': 'بطارية سيارة 12V',
        'description': 'بطارية عالية الجودة تناسب جميع السيارات الصغيرة.',
        'image': 'battery.jpg',
        'whatsapp_message': 'مرحباً، أرغب بطلب بطارية سيارة 12V من موقع Parts Hunter'
    },
    {
        'name': 'مولد كهرباء صغير',
        'description': 'مولد محمول للطوارئ.',
        'image': 'generator.jpg',
        'whatsapp_message': 'مرحباً، أرغب بطلب مولد كهرباء صغير من موقع Parts Hunter'
    },
    {
        'name': 'مبرد مياه',
        'description': 'مبرد مياه عالي الكفاءة.',
        'image': 'cooler.jpg',
        'whatsapp_message': 'مرحباً، أرغب بطلب مبرد مياه من موقع Parts Hunter'
    },
    {
        'name': 'فانوس LED',
        'description': 'مصباح LED محمول للسيارة.',
        'image': 'led_lamp.jpg',
        'whatsapp_message': 'مرحباً، أرغب بطلب فانوس LED من موقع Parts Hunter'
    }
]

# الصفحة الرئيسية
@app.route('/')
def index():
    return render_template('index.html', products=products)

# صفحة الطلب
@app.route('/order')
def order():
    return render_template('order.html')
