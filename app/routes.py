import os
import json
import uuid
from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from werkzeug.utils import secure_filename

from app.forms import UploadForm
from app.prediction import predict_skin_disease

main = Blueprint('main', __name__)

# File extensions allowed for upload
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@main.route('/', methods=['GET', 'POST'])
def index():
    """Home page with upload form"""
    form = UploadForm()
    
    if form.validate_on_submit():
        # This checks if file was uploaded
        if 'photo' not in request.files:
            flash('No file part', 'danger')
            return redirect(request.url)
        
        file = request.files['photo']
        
        # This checks if user didn't select a file
        if file.filename == '':
            flash('No selected file', 'danger')
            return redirect(request.url)
        
        # This checks file type validity
        if file and allowed_file(file.filename):
            # Create unique filename to avoid overwriting
            filename = str(uuid.uuid4()) + secure_filename(file.filename)
            
            # Ensure upload directory exists
            os.makedirs(current_app.config['UPLOAD_FOLDER'], exist_ok=True)
            
            # Save the file
            filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Redirect to the diagnosis page
            return redirect(url_for('main.diagnosis', filename=filename))
        else:
            flash('Invalid file type. Please upload a JPG, JPEG or PNG image.', 'danger')
    
    return render_template('index.html', form=form)

@main.route('/diagnosis/<filename>')
def diagnosis(filename):
    """Display diagnosis results"""
    # Get file path
    filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    
    # Check if file exists
    if not os.path.exists(filepath):
        flash('File not found', 'danger')
        return redirect(url_for('main.index'))
    
    try:
        # This load the model and make prediction
        prediction, probabilities = predict_skin_disease(
            filepath,
            current_app.config['MODEL_PATH'],
            current_app.config['CLASS_NAMES_PATH']
        )
        
        # Get disease information
        from app.disease_info import get_disease_info
        disease_info = get_disease_info()
        
        # Get information for detected disease
        disease_data = disease_info.get(prediction, {
            'description': 'Information not available',
            'recommendations': ['Consult a dermatologist for proper diagnosis'],
            'severity': 'Unknown'
        })
        
        # Create image URL for display
        image_url = url_for('static', filename=f'uploads/{filename}')
        
        # Format probabilities for display
        formatted_probs = [
            (class_name, round(prob * 100, 2))
            for class_name, prob in probabilities
        ]
        
        return render_template(
            'diagnosis.html',
            prediction=prediction,
            image_url=image_url,
            probabilities=formatted_probs,
            description=disease_data['description'],
            recommendations=disease_data['recommendations'],
            severity=disease_data['severity']
        )
    
    except Exception as e:
        flash(f'Error processing image: {str(e)}', 'danger')
        return redirect(url_for('main.index'))

@main.route('/about')
def about():
    """About page with information about the application"""
    return render_template('about.html')