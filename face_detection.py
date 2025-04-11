import cv2
import sys

# Load the pre-trained Haar Cascade Classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def try_camera(index):
    cap = cv2.VideoCapture(index)
    if cap.isOpened():
        print(f"Successfully opened camera at index {index}")
        return cap
    return None

# Try different camera indices
for i in range(3):  # Try first 3 camera indices
    cap = try_camera(i)
    if cap is not None:
        break

if cap is None:
    print("Error: Could not open any camera. Please check:")
    print("1. Camera permissions in System Settings > Privacy & Security > Camera")
    print("2. If another application is using the camera")
    print("3. If the camera is properly connected")
    print("4. Try restarting your computer")
    sys.exit(1)

print("Camera initialized successfully. Press 'q' to quit.")

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    # Check if frame was captured successfully
    if not ret:
        print("Error: Could not read frame from camera")
        print("Trying to reinitialize camera...")
        cap.release()
        cap = cv2.VideoCapture(0)
        continue
    
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the grayscale image
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    # Draw rectangles around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    
    # Display the resulting frame
    cv2.imshow('Face Detection', frame)
    
    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows() 