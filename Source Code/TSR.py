import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model

# Load the pre-trained traffic sign classification model
MODEL_PATH = "gtsrb_model.h5"  # Path to your trained model
model = load_model(MODEL_PATH)

# Define class labels (German Traffic Sign Recognition Benchmark - GTSRB)
classes = {
    0: "Speed Limit 20 km/h",
    1: "Speed Limit 30 km/h",
    2: "Speed Limit 50 km/h",
    3: "Speed Limit 60 km/h",
    4: "Speed Limit 70 km/h",
    5: "No Entry",
    6: "Stop",
    7: "Yield",
    8: "Turn Left",
    9: "Turn Right"
}

# Preprocess the image for classification
def preprocess_image(img):
    img = cv2.resize(img, (32, 32))  # Resize to match model input size
    img = img / 255.0  # Normalize pixel values
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    return img

# Initialize webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale and detect edges
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours in the frame
    contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)
        if len(approx) > 4:  # Consider sign-like shapes
            x, y, w, h = cv2.boundingRect(approx)
            sign_roi = frame[y:y+h, x:x+w]  # Extract region of interest

            if sign_roi.shape[0] > 0 and sign_roi.shape[1] > 0:
                processed_img = preprocess_image(sign_roi)
                prediction = model.predict(processed_img)
                class_index = np.argmax(prediction)
                confidence = np.max(prediction)

                if confidence > 0.7:  # Confidence threshold
                    label = classes.get(class_index, "Unknown")
                    cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 
                                0.6, (0, 255, 0), 2)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Show the output frame
    cv2.imshow("Traffic Sign Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
