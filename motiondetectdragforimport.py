import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog, messagebox

def motion_detection_with_video(frame):
    def upload_video():
        root = Toplevel(frame)
        root.withdraw() 
        video_file = filedialog.askopenfilename(title="Select a Video File", filetypes=[("Video Files", "*.mp4 *.avi *.mov *.mkv")])
        return video_file

    video_file = upload_video()
    cap = cv2.VideoCapture(video_file)

    red_box = [150, 150, 300, 300] 

    dragging = False
    start_x, start_y = -1, -1

  
    def mouse_callback(event, x, y, flags, param):
        nonlocal red_box, dragging, start_x, start_y
        
        if event == cv2.EVENT_LBUTTONDOWN:

            if red_box[0] < x < red_box[0] + red_box[2] and red_box[1] < y < red_box[1] + red_box[3]:
                dragging = True
                start_x, start_y = x - red_box[0], y - red_box[1]
        
        elif event == cv2.EVENT_MOUSEMOVE:

            if dragging:
                red_box[0] = x - start_x
                red_box[1] = y - start_y
        
        elif event == cv2.EVENT_LBUTTONUP:

            dragging = False

 
    cv2.namedWindow("Motion Detection")
    cv2.setMouseCallback("Motion Detection", mouse_callback)


    fgbg = cv2.createBackgroundSubtractorMOG2()

    while True:

        ret, frame = cap.read()
        if not ret:
            break


        fgmask = fgbg.apply(frame)


        contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


        for contour in contours:
            if cv2.contourArea(contour) > 500:
                (x, y, w, h) = cv2.boundingRect(contour)

                if (red_box[0] < x < red_box[0] + red_box[2] and 
                    red_box[1] < y < red_box[1] + red_box[3]):
                    cv2.putText(frame, "ALERT: Motion in restricted area!", (50, 50), 
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)


        cv2.rectangle(frame, (red_box[0], red_box[1]), 
                      (red_box[0] + red_box[2], red_box[1] + red_box[3]), 
                      (0, 0, 255), 2)

     
        cv2.imshow("Motion Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

