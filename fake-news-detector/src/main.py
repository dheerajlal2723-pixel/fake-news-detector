# This is the entry point of the application for the Fake News Detector.

from data.preprocess import clean_text, extract_features
from models.detector import FakeNewsDetector
from utils.helpers import log_message, load_config

def main():
    # Load configuration
    config = load_config()
    
    # Initialize the Fake News Detector
    detector = FakeNewsDetector(config['model_path'])
    
    # Load the model
    detector.load_model()
    
    log_message("Model loaded successfully.")
    
    while True:
        # Get user input
        user_input = input("Enter the news article text (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        
        # Preprocess the input
        cleaned_text = clean_text(user_input)
        features = extract_features(cleaned_text)
        
        # Make prediction
        prediction = detector.predict(features)
        
        # Output the result
        log_message(f"Prediction: {'Fake' if prediction else 'Real'}")

if __name__ == "__main__":
    main()