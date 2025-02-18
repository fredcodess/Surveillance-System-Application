import os
import ffmpeg
from tkinter import *
from tkinter import filedialog, messagebox

def mp4_video_converter(frame):
    def select_file():
        file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.avi;*.mkv;*.mov;*.flv;*.wmv;*.mp4")])
        if file_path:
            entry_file_path.delete(0, END)
            entry_file_path.insert(0, file_path)

    def convert_to_mp4():
        input_file = entry_file_path.get()
        if not input_file:
            messagebox.showerror("Error", "Please select a video file first.")
            return
        
        if not os.path.exists(input_file):
            messagebox.showerror("Error", "The selected file does not exist.")
            return
        
        output_file = os.path.splitext(input_file)[0] + "_converted.mp4"
        
        try:
            ffmpeg.input(input_file).output(output_file).run()
            
            messagebox.showinfo("Success", f"your Video was successfully converted to {output_file}")
        except Exception as e:
            messagebox.showerror("Error", f"n error occurred: {str(e)}")


    root = Toplevel(frame)
    root.title("Video Converter")
    root.geometry("500x200")
    root.configure(bg='cyan4')


    label = Label(root, text="Select a Video File", font=('Arial', 14), bg='cyan4', fg='cyan')
    label.pack(pady=10)

    entry_file_path = Entry(root, font=('Arial', 12), width=40)
    entry_file_path.pack(pady=5)

    select_button = Button(root, text="Browse", bd=5, bg='cyan3', font=('Arial', 12), command=select_file)
    select_button.pack(pady=5)

    convert_button = Button(root, text="Convert to MP4", bd=5, bg='cyan3', font=('Arial', 12), command=convert_to_mp4)
    convert_button.pack(pady=20)

    root.mainloop()
