# Temperature Conversion Model

This project uses TensorFlow to create a neural network model that converts Fahrenheit temperatures to Kelvin. It includes functionality to train the model, save it, load it for later use, and use it for predictions. The model is trained using a small dataset and can be used in interactive mode to predict Kelvin temperatures from a Fahrenheit input.

# Features

- Model Training: If no pre-trained model is found, the program trains a neural network on a small dataset of Fahrenheit-to-Kelvin conversions.
- Model Prediction: Once trained, the model can predict Kelvin values for any Fahrenheit input.
- Formula-Based Conversion: Provides a standard formula-based method for Fahrenheit-to-Kelvin conversion as a reference alongside the model-based predictions.
- Model Saving and Loading: The trained model is saved in TensorFlow's SavedModel format for easy reloading and future predictions without retraining.

# Requirements
- `Python 3.11+`
- `tensorflow>=2.13.0`
- `numpy>=1.26.1`

# Setup and Usage
### 1. Clone the Repository
- First, clone the repository to your local machine:
```
git clone https://github.com/your-username/temperature-conversion-model.git
cd temperature-conversion-model
```
### 2. Run the Program
- To run the temperature conversion model, execute the main script:
```python
python temperature_conversion_model.py
```

- If a pre-trained model is not found, the script will train a new model on the sample dataset. If an existing model is detected, it will load the model for predictions.

### 3. Interactive Input
- The program will prompt you to enter a Fahrenheit value, and it will display both the model-predicted Kelvin value and the value obtained using the standard conversion formula.

### Example interaction:

```
Enter a temperature in Fahrenheit to convert to Kelvin: 100
Using the model: 100.0 Fahrenheit is approximately 311.45 Kelvin
Using the formula: 100.0 Fahrenheit is approximately 310.93 Kelvin
```

# How It Works
### Training Phase
    A small dataset is used to train the model with the following data points:

    Fahrenheit: [-40, 14, 32, 46]
    Kelvin: [233.15, 263.15, 273.15, 280.93]
    The model uses a neural network with a dense layer and is optimized with mean squared error loss.

    Model Save and Load
    After training, the model is saved in TensorFlow's SavedModel format using model.save(). When re-run, the model will load automatically if the saved model file is present.

### Prediction Phase
    Once the model is loaded, it accepts any Fahrenheit value input from the user and predicts the corresponding Kelvin temperature.

### Formula-Based Conversion
    The standard conversion formula, included for reference, is:
    Kelvin = (Fahrenheit - 32) * (5/9) + 273.15

# Directory Structure
temperature-conversion-model\
├── temperature_conversion_model.py  # Main Python script\
└── README.md                        # Project overview and usage guide

# Youtube Tutorial For Better Understanding

![Youtube](https://www.google.com/imgres?q=neural%20network%20for%20noobs%20YouTube&imgurl=https%3A%2F%2Fi.ytimg.com%2Fvi%2FBJ385xQVVOk%2Fhq720.jpg)

[Youtube](https://www.youtube.com/watch?v=BJ385xQVVOk)

# License

[MIT](https://choosealicense.com/licenses/mit/)
# Hi, I'm Sujal Rajpoot! 👋
## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://sujalrajpoot.netlify.app/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sujal-rajpoot-469888305/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/sujalrajpoot70)


## 🚀 About Me
I'm a skilled Python programmer and experienced web developer. With a strong background in programming and a passion for creating interactive and engaging web experiences, I specialize in crafting dynamic websites and applications. I'm dedicated to transforming ideas into functional and user-friendly digital solutions. Explore my portfolio to see my work in action.
