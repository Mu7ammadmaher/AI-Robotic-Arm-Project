import cv2
import numpy as np

def detect_object_center(frame):
    """
    Detects the center of a colored object (e.g., a red ball) 
    and returns its coordinates for the robotic arm.
    """
    # Convert to HSV color space for better detection
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Define color range (Example: Red)
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        # Get the largest contour (the target object)
        c = max(contours, key=cv2.contourArea)
        M = cv2.moments(c)
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            return (cX, cY)
    return None