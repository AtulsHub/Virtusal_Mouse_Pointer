import cv2
import mediapipe as mp
import math
import pyautogui

# Initialize MediaPipe Hands and PyAutoGUI settings
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1,
                       min_detection_confidence=0.7, 
                       min_tracking_confidence=0.7)

mp_drawing = mp.solutions.drawing_utils

# Screen dimensions for cursor mapping
SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()
CAMERA_WIDTH, CAMERA_HEIGHT = 640, 480
frameR = 100

#smoothng cursor movement
smoothing = 3
pcvX,pcvY =0,0
ccvX,ccvY = 0,0

# Start video capture
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_HEIGHT)


try:
    while True:
        # Read a frame from the camera
        ret, frame = cap.read()
        if not ret:
            break
        
        # Fliping the frame horizontally 
        frame = cv2.flip(frame, 1)
        
        # Converting the frame to RGB for MediaPipe processing
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Processing the frame for hand landmarks
        result = hands.process(rgb_frame)

         # creating a rectangle 
        cv2.rectangle(frame,(frameR+5,frameR-50),(CAMERA_WIDTH-frameR, CAMERA_HEIGHT - 2*frameR),(255,0,255),2)
        
        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:

                # Getting the index finger tip coordinates
                index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
               
                # Converting index finnger value to coordinates
                fingerI_x = int((index_finger_tip.x)* CAMERA_WIDTH)
                fingerI_y = int((index_finger_tip.y)* (CAMERA_HEIGHT))
                
                # Converting middle finger value to coordinates
                fingerM_x = int((middle_finger_tip.x)* CAMERA_WIDTH)
                fingerM_y = int((middle_finger_tip.y)* (CAMERA_HEIGHT))

                #Converting thumb value to coordinates
                thumb_x = int((thumb_tip.x)* CAMERA_WIDTH)
                thumb_y = int((thumb_tip.y)* (CAMERA_HEIGHT))

                condition1 = frameR < fingerM_x < CAMERA_WIDTH - frameR
                condition2 = 50 < fingerM_y < CAMERA_HEIGHT - 200

                # Checking if the finger is inside the rectangle
                if ( condition1 and condition2):
                        
                    # Map finger position to screen coordinates
                    screen_x = int((fingerM_x - frameR) / (CAMERA_WIDTH - 2 * frameR) * SCREEN_WIDTH)
                    screen_y = int((fingerM_y - 52) / (CAMERA_HEIGHT - 250) * SCREEN_HEIGHT)

                    #smoothing cursor
                    ccvX = pcvX + (screen_x - pcvX)/smoothing
                    ccvY = pcvY + (screen_y - pcvY)/smoothing
                    
                    # Moving the cursor on the screen with smoothened values
                    pyautogui.moveTo(ccvX, ccvY)

                    pcvX,pcvY = ccvX,ccvY


                # Drawing circles an finger tips
                #cv2.circle(frame, (fingerI_x, fingerI_y), 10, (250, 0, 0), -1)
                cv2.circle(frame, (fingerM_x, fingerM_y), 10, (0, 0, 255), -1)
                
                # Drawing landmark connections
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Calculate the distance between index and middle finger 
                length = float(math.sqrt((thumb_x - fingerI_x) ** 2 + (thumb_y - fingerI_y) ** 2))

                #mouse click
                print (length)
                if 16 < length < 23:
                   

                    cv2.circle(frame, (fingerI_x, fingerI_y), 10, (0, 250, 0), -1)
                    cv2.circle(frame, (thumb_x, thumb_y), 10, (0, 250, 0), -1)

                    pyautogui.click()

        
        # Displaying the frame
        cv2.imshow("Index Finger Tracking", frame)
        
        # Exit 
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # Release all resources
    hands.close()
    cap.release()
    cv2.destroyAllWindows()
    
