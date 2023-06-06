from werkzeug.middleware.proxy_fix import ProxyFix
from src import app

app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')