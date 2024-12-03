# **Virtual Mouse Pointer**

### 🚀 **Project Overview**
The **Virtual Mouse Pointer** project allows users to control their computer's mouse pointer using hand gestures tracked by a webcam. This innovative, contactless solution leverages computer vision and gesture recognition to replace traditional input devices like a physical mouse.

---

### ✨ **Features**
- **Pointer Control**: Move the mouse pointer by tracking the position of your middle finger.  
- **Click Gestures**: Simulate left-click actions when the **index finger** and **thumb** come into contact.  
- **Dynamic Mapping**: The movement of the hand within a defined region is mapped to the entire screen.  
- **Real-Time Tracking**: Hand landmarks are detected and tracked in real-time.  
- **Custom Gestures**: Additional gestures can be implemented for advanced functionality.  

---

### 🛠️ **Technologies Used**
- **Python**: The programming backbone.  
- **OpenCV**: For capturing video and image processing.  
- **MediaPipe Hands**: For detecting and tracking hand landmarks.  
- **PyAutoGUI**: To simulate mouse pointer actions.  

---

### 🖼️ **How It Works**
1. **Hand Detection**:  
   - A webcam feed is analyzed to detect the user's hand and its key landmarks using **MediaPipe Hands**.  
   - The **middle finger tip** position is used to control the pointer.  

2. **Pointer Movement**:  
   - Hand movement is dynamically mapped from the camera frame to the screen dimensions.  

3. **Gesture-Based Clicks**:  
   - Gestures, such as bringing the **index finger** and **thumb** close together, trigger a mouse click.  

---

### 📋 **Requirements**
- Python 3.7+  
- OpenCV  
- MediaPipe  
- PyAutoGUI  

Install the required dependencies with:  
```bash
pip install opencv-python mediapipe pyautogui

▶️ How to Run
Clone the repository:

bash
Copy code
git clone https://github.com/AtulsHub/virtual-mouse-pointer.git
cd virtual-mouse-pointer
Run the program:

bash
Copy code
python virtual_mouse_pointer.py
Ensure your webcam is enabled, and keep your hand within the camera frame to start controlling the pointer.
```
### 🌟 **Future Enhancements**
- Adding gestures for right-click, scrolling, and drag-and-drop.
- Support for controlling multiple screens.
- Optimizations for faster gesture recognition.
