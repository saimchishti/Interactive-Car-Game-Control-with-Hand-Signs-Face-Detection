import cv2
import mediapipe as mp
import keyboard

# Initialize Mediapipe hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)

# Function to detect hands and return their positions
def detect_hands(frame):
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)
    hand_positions = []
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for landmark in hand_landmarks.landmark:
                x, y, _ = frame.shape
                hand_positions.append((int(landmark.x * y), int(landmark.y * x)))
    return hand_positions

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Function to detect face
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
def detect_face(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    return len(faces) > 0

# Initialize variables for keyboard control
w_pressed = False
s_pressed = False
a_pressed = False
d_pressed = False

# Main loop
while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # Flip the frame horizontally
    frame = cv2.flip(frame, 1)

    # Detect faces
    face_detected = detect_face(frame)

    # Detect hands
    hand_positions = detect_hands(frame)

    # Control keyboard based on detection
    if face_detected:
        if not w_pressed:
            keyboard.press('w')
            w_pressed = True
        if s_pressed:
            keyboard.release('s')
            s_pressed = False
    else:
        if w_pressed:
            keyboard.release('w')
            w_pressed = False
        if not s_pressed:
            keyboard.press('s')
            s_pressed = True

    if not hand_positions:  # If no hands are detected
        if a_pressed:
            keyboard.release('a')
            a_pressed = False
        if d_pressed:
            keyboard.release('d')
            d_pressed = False
    else:
        for x, y in hand_positions:
            if x < frame.shape[1] // 3:  # Left third of the screen
                if not a_pressed:
                    keyboard.press('a')
                    a_pressed = True
                cv2.line(frame, (x, y), (x+20, y), (0, 255, 0), 2)  # Draw line on left hand
            elif x > 2 * frame.shape[1] // 3:  # Right third of the screen
                if not d_pressed:
                    keyboard.press('d')
                    d_pressed = True
                cv2.line(frame, (x, y), (x+20, y), (0, 0, 255), 2)  # Draw line on right hand

    # Draw rectangle around face
    if face_detected:
        faces = face_cascade.detectMultiScale(frame, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display the frame
    cv2.imshow('Frame', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
