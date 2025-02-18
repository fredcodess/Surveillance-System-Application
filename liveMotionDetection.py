import cv2
import numpy as np
import threading
import winsound

def motion_detection_with_red_box():
    cap = cv2.VideoCapture(0)

    red_box = [150, 150, 300, 300]

    dragging = False
    start_x, start_y = -1, -1

    def mouse_callback(event, x, y, flags, param):
        nonlocal start_x, start_y, red_box, dragging
        
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

    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('motion_detected.avi', fourcc, 20.0, (frame_width, frame_height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        fgmask = fgbg.apply(frame)

        contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        motion_detected = False

        for contour in contours:
            if cv2.contourArea(contour) > 500:
                (x, y, w, h) = cv2.boundingRect(contour)
                if (red_box[0] < x < red_box[0] + red_box[2] and 
                    red_box[1] < y < red_box[1] + red_box[3]):
                    cv2.putText(frame, "ALERT: Motion DETECTED in restricted area!", (50, 50), 
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    motion_detected = True

        if motion_detected:
            winsound.Beep(1000, 500)
            out.write(frame)

        cv2.rectangle(frame, (red_box[0], red_box[1]), 
                      (red_box[0] + red_box[2], red_box[1] + red_box[3]), 
                      (0, 0, 255), 2)

        cv2.imshow("Motion Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()



def start_live_cam():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Failed to grab frame.")
            break

        cv2.imshow('Live Webcam', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def motion_detection_with_red_box_bb(cap1):
    red_box = [150, 150, 300, 300]
    dragging = False
    start_x, start_y = -1, -1

    def mouse_callback(event, x, y, flags, param):
        nonlocal start_x, start_y, red_box, dragging
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
        ret, frame = cap1.read()
        if not ret:
            break

        fgmask = fgbg.apply(frame)
        contours, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv2.contourArea(contour) > 500:
                (x, y, w, h) = cv2.boundingRect(contour)
                if (red_box[0] < x < red_box[0] + red_box[2] and red_box[1] < y < red_box[1] + red_box[3]):
                    cv2.putText(frame, "ALERT: Motion DETECTED in restricted area!", (50, 50), 
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.rectangle(frame, (red_box[0], red_box[1]), 
                      (red_box[0] + red_box[2], red_box[1] + red_box[3]), 
                      (0, 0, 255), 2)

        cv2.imshow("Motion Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap1.release()


def facial_detection(cap2):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    while True:
        ret, frame = cap2.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(frame, "Face Detected", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

        cv2.imshow("Facial Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap2.release()


def run_multiple_cams():
    cap1 = cv2.VideoCapture(0)
    cap2 = cv2.VideoCapture(1)

    if not cap1.isOpened():
        print("Error: Could not open the first webcam.")
        return
    if not cap2.isOpened():
        print("Error: Could not open the second webcam.")
        return

    thread1 = threading.Thread(target=motion_detection_with_red_box_bb, args=(cap1,))
    thread2 = threading.Thread(target=facial_detection, args=(cap2,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    cv2.destroyAllWindows()


