from flask import Flask
from flask_bootstrap import Bootstrap

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key-here'  
    app.config['UPLOAD_FOLDER'] = 'app/static/uploads'
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  
    
    app.config['MODEL_PATH'] = 'data/models/final_model.pth' 
    app.config['CLASS_NAMES_PATH'] = 'data/models/class_names.json'
    
    Bootstrap(app)
    
    
    from app.routes import main
    app.register_blueprint(main)
    
    return app