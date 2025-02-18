from tkinter import *
from tkinter import messagebox
from videoPlayer import create_video_player
from LiveFeed import live_feed_options
from convertor import mp4_video_converter
from motiondetectdragforimport import motion_detection_with_video
from yolo import motion_detection_with_red_box_yolo

def check_credentials():
    username = entry_username.get()
    password = entry_password.get()
    
    if username == "admin" and password == "admin123":
        root.destroy()
        top = Tk()
        top.configure(bg='cyan4')
        top.geometry("1200x500")
        
        def openImportVideoWindow():
            create_video_player(top)

        def openLiveFeedWindow():
            live_feed_options(top)

        def openFileConverterWindow():
            mp4_video_converter(top)
            
        def uploadWithMotion():
            motion_detection_with_video(top)
            
        def objectDetection():
            motion_detection_with_red_box_yolo(top)

        import_video_button = Button(top, text="IMPORT VIDEO", width=18, height=3, font=('Arial', 20), bd=5 , bg='cyan3', command=openImportVideoWindow)
        import_video_button.place(x=20, y=100)
        
        upload_video_button = Button(top, text="UPLOAD VIDEO", width=18, height=3, font=('Arial', 20), bd=5 , bg='cyan3', command=uploadWithMotion)
        upload_video_button.place(x=20, y=300)
        
        object_detection_button = Button(top, text="OBJECT DETECTION/CLASSIFIER", width=30, height=3, font=('Arial', 20), bd=5 , bg='cyan3', command=motion_detection_with_red_box_yolo)
        object_detection_button.place(x=370, y=300)
        
        top_label_info = Label(top, text='Use "Q" on your keyboard to close live cam frames', bd=5, bg='cyan4', fg='cyan', font=('Arial', 24))
        top_label_info.place(x=200, y=440)
        
        top_label_title = Label(top, text='DASHBOARD', bd=5, bg='cyan4', fg='cyan', font=('Arial', 30))
        top_label_title.place(x=500, y=30)

        live_feed_button = Button(top, text="LIVE FEED", width=10, height=3, font=('Arial', 20), bd=5 , bg='cyan3', command=openLiveFeedWindow)
        live_feed_button.place(x=370, y=100)

        file_converter_button = Button(top, text="FILE CONVERTER", width=18, height=3, font=('Arial', 20), bd=5 , bg='cyan3', command=openFileConverterWindow)
        file_converter_button.place(x=600, y=100)

        close_button = Button(top, text="CLOSE", width=10, height=3, font=('Arial', 20), bd=5 , bg='cyan3', command=top.destroy)
        close_button.place(x=950, y=100)

        top.mainloop()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

root = Tk()
root.configure(bg='cyan4')
root.geometry("800x400")

top_label = Label(root, text='Security Login', bd=5, bg='cyan4', fg='cyan', font=('Arial', 24))
top_label.place(x=320, y=20)

label_username = Label(root, text="Username:", fg='white', bg='cyan4', font=('Arial', 20))
label_username.place(x=150, y=100)

entry_username = Entry(root, font=('Arial', 20))
entry_username.place(x=350, y=100)


label_password = Label(root, text="Password:", bg='cyan4', fg='white', font=('Arial', 20))
label_password.place(x=150, y=160)

entry_password = Entry(root, show="*", font=('Arial', 20))
entry_password.place(x=350, y=160)


login_button = Button(root, text="Login", font=('Arial', 20), bd=5 , bg='cyan3', command=check_credentials)
login_button.place(x=350, y=260)

root.mainloop()
