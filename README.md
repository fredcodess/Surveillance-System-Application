# Surveillance System Application

A Python-based application for video analysis, live monitoring, and object detection with features like motion detection, file conversion, and more.

## Installation

1. **Python Requirements**:  
   Ensure you have Python 3.6 or later installed. Verify using:

   ```bash
   python --version
   ```

2. **Install Dependencies**:  
   Install required libraries using `pip`:
   ```bash
   pip install opencv-python numpy winsound pyqt5
   ```

---

## Running the Application

1. **Navigate to the Project Directory**:  
   Open a terminal and go to the project folder:

   ```bash
   cd path/to/project-folder
   ```

2. **Launch the Application**:  
   Run the main script:

   ```bash
   python login.py
   ```

   _If the command fails, try `python3 login.py`._

3. **Log In**:

   - Use the default credentials:  
     **Username**: `admin`  
     **Password**: `admin123`
   - Click the **Login** button to access the dashboard.

4. **Dashboard Features**:  
   After logging in, you can:

   - **Import Videos**: Analyze pre-recorded footage.
   - **Live Feed**: Monitor real-time camera streams.
   - **File Converter**: Convert video formats.
   - **Motion Detection**: Detect motion in uploaded videos.
   - **Upload Video**: Upload and track motion in videos.
   - **Object Detection**: Use YOLO and live cameras to detect humans in restricted areas (triggers alarms via `winsound`).

5. **Exit the Application**:
   - Press the `Q` key to close live feeds.
   - Click the **Close** button or close the window to exit.

---

## Troubleshooting

- **Python Not Found**:  
  Ensure Python is installed and added to your system’s PATH.

- **Missing Modules**:  
  Install missing libraries using:

  ```bash
  pip install <library-name>
  ```

- **Live Feed/Camera Issues**:

  - Confirm the camera is connected and accessible.
  - Grant camera permissions if prompted by your OS.

- **YOLO Errors**:  
  Ensure YOLO model files ( `yolov3.weights`, `yolov3.cfg`, `coco.names`) are in the correct directory.

- **GUI Rendering Problems**:  
  Update PyQt or reinstall it:
  ```bash
  pip install --upgrade pyqt5
  ```

---

**Note**: For security, change the default login credentials in the code before deployment.
