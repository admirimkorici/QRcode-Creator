import pyqrcode  
data = input('Vendosni linkun e QRcode qe doni te lexoni')
qr = pyqrcode.QRCode(data)
text = qr.terminal()
print(text)