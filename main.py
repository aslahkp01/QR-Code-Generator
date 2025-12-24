import qrcode

url=input("Enter your URL :").strip()
if not url:
    print(" URL cannot be empty")
    exit()
file_path = input("Enter file name (without .png): ").strip()
if not file_path:
    file_path = "qrcode"
file_path += ".png"

qr=qrcode.QRCode()
qr.add_data(url)

img=qr.make_image()
img.save(file_path)

print("QR Code was Succesfully Genarated")