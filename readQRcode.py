# Importing the required modules
import pyqrcode  
# data to be inserted in the QR Code
data = 'https://www.codeunderscored.com/'
# creating the QR Code object with the data
qr = pyqrcode.QRCode(data)
# using the terminal method to get the text for QR code
text = qr.terminal()
# displaying the QR Code
print(text)