import numpy as np
import cv2
from PIL import ImageGrab
import pyautogui

while(True):
    # Capture the screen
    screen = np.array(ImageGrab.grab(bbox=None)) # bbox specifies specific region (bbox=x1,y1,x2,y2)
    gray_screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

    # Your logic to locate the game window and detect grid cells
    # ...

    # Display the captured screen (for debugging purposes)
    cv2.imshow('window', gray_screen)

    # Your logic to control the mouse based on cell detection
    # ...

    # Press 'q' to quit the loop
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
