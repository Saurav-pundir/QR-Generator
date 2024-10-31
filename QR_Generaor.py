import qrcode
from PIL import Image
import os
from urllib.parse import urlparse

# Get the website URL from the user
website = input("Enter your Website to generate QR Code: ")

# Extract the domain name
parsed_url = urlparse(website)
domain_parts = parsed_url.netloc.split('.')
if domain_parts[0] == 'www':
    domain_name = domain_parts[1]
else:
    domain_name = domain_parts[0]

# Create an instance of QRCode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# Add data to the QR Code
qr.add_data(website)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill_color="white", back_color="black")

# Save the generated QR Code as an image file with the domain name
filename = f"{domain_name}.png"
img.save(filename)

print(f"QR Code saved as {filename}")
