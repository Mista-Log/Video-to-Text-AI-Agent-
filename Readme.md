# Video Text Extraction Using Python & Tesseract OCR

## 📌 Overview
This script extracts **all** text (including duplicates) from a video by processing its frames and using Tesseract OCR for text recognition. The extracted text is saved in a file named `Output.txt` in the same directory as the script.

---

## 🔧 Prerequisites
Ensure you have the following installed on your system before running the script:

### 1️⃣ **Python Installation**
Make sure you have Python installed. If not, download and install it from:
- [Python Official Website](https://www.python.org/downloads/)

After installation, verify it using:
```sh
python --version
```

### 2️⃣ **Install Required Python Packages**
Install the necessary dependencies using pip:
```sh
pip install opencv-python pytesseract
```

### 3️⃣ **Download & Install Tesseract OCR**
Tesseract OCR is required for extracting text from images.

#### 📥 **Download Tesseract for Windows**:
1. Visit: [Tesseract OCR Download](https://github.com/UB-Mannheim/tesseract/wiki)
2. Download the Windows installer (`tesseract-ocr-setup.exe`).
3. Install it, and **note the installation path** (e.g., `C:\Program Files\Tesseract-OCR`).

#### 🔧 **Add Tesseract to System PATH (Windows Only)**
1. Open **Windows Search** and type `Environment Variables`.
2. Click on **Edit the system environment variables**.
3. Under **System variables**, find **Path**, then click **Edit**.
4. Click **New**, and add:  
   `C:\Program Files\Tesseract-OCR`
5. Click **OK** to save changes.
6. Test if Tesseract is working by running this command in **Command Prompt (cmd)**:
   ```sh
   tesseract --version
   ```
   If installed correctly, it will show version details.

---

## 🚀 Running the Script
### 1️⃣ **Place the video file**
Ensure your video file is placed in the same directory as your script or specify the correct path.

### 2️⃣ **Modify the script to set Tesseract Path**
If Tesseract is **not in your PATH**, add this line at the beginning of your script:
```python
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```
Make sure the path matches where you installed Tesseract.

### 3️⃣ **Run the script**
Execute the Python script by running:
```sh
python video_to_text.py
```
After execution, you will see:
```sh
Text extraction complete! Check 'Output.txt' for results.
```

---

## 📂 Output
- **Extracted text** (including duplicates) will be saved in a file named `Output.txt` inside the same directory as the script.

---

## 🛠 Customization & Enhancements
- **Process every frame**: Remove `if frame_count % 10 == 0:` to extract text from all frames.
- **Save unique text only**: Store text in a Python `set()` before writing to the file.
- **Improve OCR Accuracy**: Preprocess frames (convert to grayscale, increase contrast, etc.).

---

## 🤝 Support
If you encounter any issues, ensure:
1. Python, OpenCV, and Tesseract are correctly installed.
2. The correct Tesseract path is used.
3. The video file is accessible and readable.

Happy coding! 🚀

