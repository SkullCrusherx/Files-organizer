🗂️ File Organizer GUI
A simple yet powerful file organizer built with Python, Tkinter, and OS module, designed to help you declutter your folders with ease. Move files into folders based on extension, keyword, or custom rules—all from a user-friendly interface. 

<!-- Optional: replace with actual image path -->

🚀 Features
Graphical User Interface using Tkinter

Organize files by extension (e.g., .jpg, .pdf, .mp4)

Supports keyword-based file sorting

Optional subfolder creation by date or type

Lightweight and cross-platform

Designed with threading for smooth UI during operations

📸 Interface Preview
> (Insert a screenshot in the icon/ folder and update the path in the image above.)

🧩 Requirements
Python 3.7+

OS module (standard with Python)

Tkinter (usually bundled with Python; installable via OS package manager if missing)

🔧 Installation
bash
git clone https://github.com/SkullCrusherx/Files-organizer.git
cd file-organizer-gui
python organizer.py
🖱️ Usage
Launch the app.

Select a target folder using the "Browse" button.

Choose the organization method (by extension, keyword, or date).

Click “Organize” to tidy up your files.

📁 Directory Structure
plaintext
file-organizer-gui/
│
├── organizer.py         # Main GUI application
├── icon/
│   └── icon.ico         # App icon (used with pyinstaller or displayed in UI)
├── README.md
└── requirements.txt     # Optional: include if extra packages are needed
📦 Packaging to EXE (Windows)
To convert into an executable with a custom icon:

bash
pyinstaller --onefile --noconsole --icon=icon/icon.ico organizer.py
📜 License
MIT License. See LICENSE for more info.
