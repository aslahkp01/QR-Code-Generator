📱 QR Code Generator (Python)

A simple and user-friendly QR Code Generator built using Python.

This project allows users to generate customizable QR codes for any URL or text and save them as image files.

🚀 Features

✅ Generate QR codes for any URL or text

🎨 Customizable size, border, and colors

🛡 High error correction for better scanning reliability

📁 User-defined output file name

🧹 Clean, modular, and beginner-friendly code

🛠 Tech Stack

Language: Python

Library: qrcode

Image Backend: Pillow (installed automatically)

📦 Installation

1️⃣ Clone the repository

git clone https://github.com/aslahkp01/QR-Code-Generator.git
cd QR-Code-Generator

2️⃣ Install dependencies

pip install qrcode[pil]

▶️ Usage

Run the script:

python qr_generator.py

Example Input:

Enter your URL: https://github.com/aslahkp01

Enter file name (without .png): github_qr

Output:

✅ QR Code successfully generated!


A file named github_qr.png will be created in the project directory.

🧠 How It Works (Brief)

Takes user input (URL/text)

Creates a QR code object with custom settings

Converts the QR data into an image

Saves the image as a .png file

🧪 Customization Options

You can easily customize:

QR size (box_size)

Error correction level

Colors (fill_color, back_color)

Output file name

📈 Future Improvements

🔹 Add GUI using Tkinter

🔹 Generate QR for WiFi, Email, WhatsApp

🔹 Add logo inside QR code

🔹 Convert to a web app using Flask

🤝 Contributing

Contributions are welcome!

Feel free to fork the repo, improve features, and submit a pull request.

📜 License

This project is open-source and available under the MIT License.

👤 Author

Muhammad Aslah

GitHub: https://github.com/aslahkp01

⭐ If you like this project, don’t forget to star the repository!
