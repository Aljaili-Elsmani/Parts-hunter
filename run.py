from app import app

if __name__ == "__main__":
    # debug=True لتسهيل التطوير، في الإنتاج يمكن تغييره إلى False
    app.run(debug=True, host='0.0.0.0', port=5000)
