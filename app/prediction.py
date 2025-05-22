import json
import numpy as np
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image

def predict_skin_disease(image_path, model_path, class_names_path):
    """
    Make prediction on a skin image using PyTorch model.
    
    Args:
        image_path (str): Path to the uploaded image
        model_path (str): Path to the trained PyTorch model
        class_names_path (str): Path to the class names JSON file
        
    Returns:
        tuple: (predicted_class_name, list of (class_name, probability) tuples)
    """
    
    # Set device
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    
    # Load class names
    with open(class_names_path, 'r') as f:
        class_names = json.load(f)
    
    # Load model checkpoint
    checkpoint = torch.load(model_path, map_location=device)
    
    # Initialize model architecture (ResNet50)
    model = models.resnet50(pretrained=False)
    num_ftrs = model.fc.in_features
    model.fc = nn.Sequential(
        nn.Dropout(0.3),
        nn.Linear(num_ftrs, len(class_names))
    )
    
    # Load model weights
    if 'model_state_dict' in checkpoint:
        model.load_state_dict(checkpoint['model_state_dict'])
        # Get normalization values from checkpoint if available
        mean = checkpoint.get('mean', torch.tensor([0.5704, 0.4474, 0.4105]))
        std = checkpoint.get('std', torch.tensor([0.1814, 0.1598, 0.1579]))
    else:
        model.load_state_dict(checkpoint)
        # Use default values
        mean = torch.tensor([0.5704, 0.4474, 0.4105])
        std = torch.tensor([0.1814, 0.1598, 0.1579])
    
    model = model.to(device)
    model.eval()
    
    # Define image transforms
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=mean.tolist(), std=std.tolist())
    ])
    
    # Load and preprocess image
    image = Image.open(image_path).convert('RGB')
    image_tensor = transform(image).unsqueeze(0).to(device)
    
    # Make prediction
    with torch.no_grad():
        outputs = model(image_tensor)
        probabilities = torch.nn.functional.softmax(outputs[0], dim=0)
    
    # Get top prediction
    predicted_class_index = torch.argmax(probabilities).item()
    predicted_class_name = class_names[predicted_class_index]
    
    # Get all class probabilities
    class_probabilities = [(class_names[i], float(prob)) for i, prob in enumerate(probabilities)]
    
    # Sort by probability (descending)
    class_probabilities.sort(key=lambda x: x[1], reverse=True)
    
    return predicted_class_name, class_probabilities