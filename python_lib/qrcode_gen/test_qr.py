from qr_lib import QRCodeGenarator


qr_gen = QRCodeGenarator(version=1, box_size=10, border=5)

# Generate QR code and save it on a file path
# qr_gen.generate_qr('https://belloibrahv.vercel.app', 'test.png')

# Display QR code from given data
qr_gen.display_qr('Hello, World!')
