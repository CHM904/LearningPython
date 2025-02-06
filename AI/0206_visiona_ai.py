import cv2
import numpy as np
import tensorflow as tf

# Load pre-trained MobileNet model and labels
model = tf.keras.applications.MobileNetV2(weights='imagenet', include_top=True)
class_names = open('imagenet_classes.txt').read().splitlines()

# Load an image
image_path = 'car01.jpg'  # Provide the path to your image file
image = cv2.imread(image_path)

def preprocess_image(image):
    image_resized = cv2.resize(image, (224, 224))
    image_array = np.expand_dims(image_resized, axis=0)
    image_preprocessed = tf.keras.applications.mobilenet_v2.preprocess_input(image_array)
    return image_preprocessed

preprocessed_image = preprocess_image(image)

predictions = model.predict(preprocessed_image)
predicted_class = np.argmax(predictions, axis=1)
predicted_class_name = class_names[predicted_class[0]]

print(f'Detected object: {predicted_class_name}')

cv2.putText(image, predicted_class_name, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
cv2.imshow('Image Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
# End of AI/0206_visiona_ai.py