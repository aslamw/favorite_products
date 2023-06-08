from werkzeug.middleware.proxy_fix import ProxyFix
from src import app, db

app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
    app.run(debug=True, port=6060, host='0.0.0.0')