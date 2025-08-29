# 🐾 Animal & File Viewer (Flask App)

This is a simple web application built using **Flask** and **HTML/CSS/JavaScript** that allows users to:

- ✅ Select one of three animals (Cat, Dog, Elephant) via checkboxes
- ✅ Upload any file from their device
- 🖼️ Display a locally stored image of the selected animal
- 📁 Show file name, size, and type of the uploaded file

---

## 📦 Features

- **Checkbox Selection**: Choose between Cat, Dog, or Elephant
- **File Upload**: Upload any file and get instant feedback
- **Dynamic Image Display**: Shows the selected animal's image
- **File Metadata**: Displays uploaded file’s name, size (in bytes), and MIME type

---

## 🧰 Tech Stack

| Layer     | Technology         |
|-----------|--------------------|
| Frontend  | HTML, CSS, JavaScript |
| Backend   | Flask (Python)     |
| Storage   | Local file system  |

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/YOUR_USERNAME/animal-file-viewer.git
cd animal-file-viewer

### 2. Set Up Python Environment
bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

###3. Install Dependencies
bash
pip install flask

###4. Run the App
bash
python app.py
You should see output like:

Code
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
Then open your browser and visit: http://127.0.0.1:5000

📁 Folder Structure
Code
animal-file-viewer/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── images/
│       ├── cat.jpg
│       ├── dog.jpg
│       └── elephant.jpg
├── uploads/
