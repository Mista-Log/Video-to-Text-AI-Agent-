import cv2
import pytesseract
import os

# Set the path to Tesseract (if not in PATH)
pytesseract.pytesseract.tesseract_cmd = r"path\to\Tesseract-OCR\tesseract.exe"

# Load the video file
video_path = r"path/to/your/video.mp4"  # Update this with your video path
video_capture = cv2.VideoCapture(video_path)

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
output_file_path = os.path.join(script_dir, "Output.txt")

# Open the file for writing
with open(output_file_path, "w", encoding="utf-8") as file:
    frame_count = 0
    success, frame = video_capture.read()

    while success:
        if frame_count % 10 == 0:  # Process every 10th frame to speed up
            text = pytesseract.image_to_string(frame).strip()
            if text:
                file.write(text + "\n")  # Write text to file including duplicates
        success, frame = video_capture.read()
        frame_count += 1

# Release the video
video_capture.release()

print(f"Text extraction complete! Check '{output_file_path}' for results.")
