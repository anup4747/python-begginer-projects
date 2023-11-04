import qrcode

# Data to encode
data = "https://replit.com/~"

# Generate QR code
img = qrcode.make(data)

# Specify the file path for the QR code image
file_path =r"C:\Users\Deepu\Desktop\Programming\python d\Projects\qr\qr.png"

# Save QR code as PNG file at the specified location
img.save(file_path)
