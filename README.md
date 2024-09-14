# Face and Hand Detection Control System for Crazy Cars Game

This project uses face and hand detection to control the game "Crazy Cars." The system utilizes OpenCV and MediaPipe to detect facial and hand movements, which are mapped to specific keyboard controls to interact with the game.

## Controls

- **Face Detection:**
  - When a face is detected, the 'W' key is pressed.
  - When nothing is detected, the 'S' key is pressed.

- **Hand Detection:**
  - Right hand detection presses the 'D' key.
  - Left hand detection presses the 'A' key.

## How to Run

1. **Download the Game**
   - Download "Crazy Cars" from the following link:
     - [Crazy Cars Download](https://www.gametop.com/download-free-games/crazy-cars/)

2. **Install Necessary Libraries**
   - Open a terminal or command prompt and install the required Python libraries:
     ```bash
     pip install opencv-python mediapipe keyboard
     ```

3. **Run the Game and the Code**
   - Start the "Crazy Cars" game.
   - Run the face and hand detection control code simultaneously to start controlling the game using face and hand gestures.
   
## Additional Notes

- Ensure your webcam is connected and working properly, as the program relies on real-time video input for face and hand detection.
- Adjust the lighting in your environment for better detection accuracy.
