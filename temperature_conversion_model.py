import tensorflow as tf
import numpy as np
import os

class TemperatureConversionModel:
    def __init__(self, model_path):
        self.model_path = model_path
        self.model = None
        
    def _train_model(self, fahrenheit_q, kelvin_a):
        """Internal method to train the model."""
        nn = tf.keras.layers.Dense(units=1, input_shape=[1])
        self.model = tf.keras.Sequential([nn])
        self.model.compile(loss="mean_squared_error", optimizer=tf.keras.optimizers.Adam(0.1))
        
        # Train the model
        self.model.fit(fahrenheit_q, kelvin_a, epochs=9450, verbose=True)
        self.model.save(self.model_path)
        
    def _load_model(self):
        """Internal method to load the pre-trained model."""
        if os.path.exists(self.model_path):
            self.model = tf.keras.models.load_model(self.model_path)
            print("Model Loaded Successfully.\n")
        else:
            raise FileNotFoundError(f"The model file does not exist at {self.model_path}.")
    
    def train_or_load_model(self):
        """Check if model exists; if not, train it."""
        if not os.path.exists(self.model_path):
            # Data for training
            fahrenheit_q = np.array([-40, 14, 32, 46])
            kelvin_a = np.array([233.15, 263.15, 273.15, 280.928])
            
            # Train the model if not found
            print("Training the model...")
            self._train_model(fahrenheit_q, kelvin_a)
        else:
            # Load the pre-trained model
            self._load_model()

    @staticmethod
    def fahrenheit_to_kelvin_formula(fahrenheit):
        """Convert Fahrenheit to Kelvin using the formula."""
        return (fahrenheit - 32) * (5/9) + 273.15

    def predict_kelvin(self, fahrenheit_input):
        """Predict the Kelvin value using the trained model."""
        return self.model.predict([fahrenheit_input])[0][0]

def main():
    model_path = r"/temperature_conversion_model"
    temperature_converter = TemperatureConversionModel(model_path)
    
    # Train or load the model
    temperature_converter.train_or_load_model()
    
    while True:
        try:
            # Get user input for Fahrenheit value
            fahrenheit_input = float(input("Enter a temperature in Fahrenheit to convert to Kelvin: "))
            
            # Predict the Kelvin value using the model
            predicted_kelvin = temperature_converter.predict_kelvin(fahrenheit_input)
            
            # Calculate the Kelvin value using the formula
            calculated_kelvin = TemperatureConversionModel.fahrenheit_to_kelvin_formula(fahrenheit_input)
            
            # Print both the predicted and formula-calculated Kelvin values
            print(f"Using the model: {fahrenheit_input} Fahrenheit is approximately {predicted_kelvin:.2f} Kelvin")
            print(f"Using the formula: {fahrenheit_input} Fahrenheit is approximately {calculated_kelvin:.2f} Kelvin\n")
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
