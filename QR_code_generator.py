import qrcode

data = input("Enter text or URL: ")

qr = qrcode.QRCode(
    box_size=10,   # QR এর সাইজ 
    border=4       # চারপাশের সাদা বর্ডার
)
qr.add_data(data)
qr.ke(fit=True)

img = qr.make_image(fill_color="blue", back_color="white")
img.save("qr_code.png")

print("QR code saved as qr_code.png")