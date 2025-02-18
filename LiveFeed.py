import tkinter as tk
from tkinter import Button
from liveMotionDetection import motion_detection_with_red_box
from liveMotionDetection import start_live_cam
from liveMotionDetection import run_multiple_cams

def live_feed_options(root):

    live_feed_window = tk.Toplevel(root)
    live_feed_window.title("Live Cameras Window")
    live_feed_window.configure(bg='cyan4')
    live_feed_window.geometry("400x400")

    def trackLiveMotionsWindow():
        motion_detection_with_red_box()
        
    def startLiveCamWindow():
        start_live_cam()
        
    def multipleLiveFeedWindow():
        run_multiple_cams()
        
    def closeWindow():
        live_feed_window.destroy()
        
        
    openbtn = Button(live_feed_window, text="LIVE MOTION DETECTION", font=('Arial', 20), bd=5 , bg='cyan3', width=23, command=trackLiveMotionsWindow)
    openbtn.pack(pady=10)

    closebtn = Button(live_feed_window, text="START LIVE CAM", font=('Arial', 20), bd=5 , bg='cyan3', width=20, command=startLiveCamWindow)
    closebtn.pack(pady=10)

    closebtn = Button(live_feed_window, text="MULTIPLE LIVE CAMS", font=('Arial', 20), bd=5 , bg='cyan3', width=20, command=multipleLiveFeedWindow)
    closebtn.pack(pady=10)

    closebtn = Button(live_feed_window, text="CLOSE", font=('Arial', 20), bd=5 , bg='cyan3', width=10, command=closeWindow)
    closebtn.pack(pady=10)
