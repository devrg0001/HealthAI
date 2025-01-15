import tensorflow as tf
import numpy as np
import os
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt

# Load the pre-trained model
model = tf.keras.models.load_model('website/Lung_Cancer_model_3.h5')  # Adjust the path as needed

# Class labels
class_labels = ['Benign', 'Malignant', 'Normal']

def runLungCancer(input_image):
    # Load the image and preprocess it
    img = input_image.resize((150, 150))    # Resize image to match the input size of your model
    img_array = image.img_to_array(img)  # Convert the image to a numpy array
    img_array = np.expand_dims(img_array, axis=0)  # Add a batch dimension
    img_array = img_array / 255.0  # Rescale the pixel values to [0, 1] 

    # Make a prediction
    predictions = model.predict(img_array)

    # Get the predicted class
    predicted_class = np.argmax(predictions, axis=1)[0]


    # Display the result
    '''
    plt.imshow(img)
    plt.title(f'Predicted: {class_labels[predicted_class]}')
    plt.axis('off')
    plt.show()
    '''
    # Print the prediction
    return class_labels[predicted_class]