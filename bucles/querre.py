import qrcode
import os

url = input("Enter the URL: ").strip()
file_path = "C:\\Users\\mavar\\OneDrive\\Desktop\\qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("QR Code was generated!")