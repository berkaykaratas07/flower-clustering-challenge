import numpy as np
import os
from keras.preprocessing import image
from tensorflow.keras.applications import Xception
from tensorflow.keras.applications.xception import preprocess_input
from keras.models import Model

# Load the Xception model and set it to extract features from the 'avg_pool' layer
base_model = Xception(weights='imagenet')
model = Model(inputs=base_model.input, outputs=base_model.get_layer('avg_pool').output)

def extract_features(image_path, model):
    """Extracts features from an image file."""
    img = image.load_img(image_path, target_size=(299, 299))  # Input size (299, 299) for Xception
    img_array = image.img_to_array(img)
    preprocessed_img = preprocess_input(np.expand_dims(img_array, axis=0))
    features = model.predict(preprocessed_img)
    return features.flatten()

def extract_features_from_folder(folder_path, model):
    """Extracts features from all images in a folder."""
    features = []
    for class_name in sorted(os.listdir(folder_path)):
        class_folder = os.path.join(folder_path, class_name)
        for image_file in os.listdir(class_folder):
            image_path = os.path.join(class_folder, image_file)
            features.append(extract_features(image_path, model))
    return np.array(features)

# Extract features and save
folder_path = 'C:\\Users\\Berkay\\Desktop\\flower\\flower_photos'
features = extract_features_from_folder(folder_path, model)
np.save('C:\\Users\\Berkay\\Desktop\\model', features)