from app import app
import os

if __name__ == "__main__":
    # Render يحتاج استخدام host='0.0.0.0' و port من متغير البيئة
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
