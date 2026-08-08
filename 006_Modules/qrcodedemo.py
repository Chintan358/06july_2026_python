import qrcode

# Configure the QR code specifications
qr = qrcode.QRCode(
    version=1,                           # Size size matrix (1 is 21x21, up to 40)
    error_correction=qrcode.constants.ERROR_CORRECT_M, # Fixes ~15% of damage
    box_size=10,                         # Pixel width/height of each box
    border=4,                            # Minimum thickness of the border
)

# Populate data
data = "https://www.tops-int.com/"
qr.add_data(data)
qr.make(fit=True)

# Generate image with custom colors
img = qr.make_image(fill_color="darkblue", back_color="white")

# Save the final file
img.save("custom_qr.png")
