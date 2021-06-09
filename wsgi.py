from app import app
from app_config import APP_HOST, APP_PORT

if __name__ == '__main__':
    app.run(
        host=APP_HOST,
        port=APP_PORT,
        debug=True
    )
