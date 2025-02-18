import cv2
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk
from motiondetectdragforimport import motion_detection_with_video

def create_video_player(root):
    video_window = tk.Toplevel(root)
    video_window.configure(bg='cyan4')
    video_window.title("Video Player")
    video_window.geometry("800x600")

    video_path = None
    cap = None
    playing = False

    video_label = tk.Label(video_window)
    video_label.pack()

    def choose_video():
        nonlocal video_path, cap
        video_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi;*.mov;*.mkv")])
        if video_path:
            cap = cv2.VideoCapture(video_path)
            ret, frame = cap.read()
            if ret:
                show_frame(frame)

    def play_video():
        nonlocal playing
        if cap is None:
            return
        playing = True
        update_frame()

    def stop_video():
        nonlocal playing
        playing = False

    def replay_video():
        nonlocal cap, playing
        if cap is None:
            return
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        playing = True
        update_frame()

    def update_frame():
        nonlocal cap, playing
        if playing:
            ret, frame = cap.read()
            if ret:
                show_frame(frame)
                video_window.after(30, update_frame)
            else:
                stop_video() 

    def show_frame(frame):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (700, 400))
        img = Image.fromarray(frame)
        imgtk = ImageTk.PhotoImage(image=img)
        video_label.imgtk = imgtk
        video_label.config(image=imgtk)

    button_frame = tk.Frame(video_window, bg='cyan4')
    button_frame.pack(pady=20)

    choose_button = ttk.Button(button_frame, text="Choose Video", command=choose_video)
    choose_button.grid(row=0, column=0, padx=10)

    play_button = ttk.Button(button_frame, text="Play", command=play_video)
    play_button.grid(row=0, column=1, padx=10)

    stop_button = ttk.Button(button_frame, text="Stop", command=stop_video)
    stop_button.grid(row=0, column=2, padx=10)

    replay_button = ttk.Button(button_frame, text="Replay", command=replay_video)
    replay_button.grid(row=0, column=3, padx=10)
    
    closebtn = ttk.Button(button_frame, text="CLOSE", width=10, command=video_window.destroy)
    closebtn.grid(row=0, column=4, padx=10)
