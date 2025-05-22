from app import create_app
import os

app = create_app()

if __name__ == '__main__':
    os.makedirs('app/static/uploads', exist_ok=True)
    os.makedirs('data/models', exist_ok=True)
    
    
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True 
    )