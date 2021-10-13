import qrcode

def image_qr(content):
    filename = input('Emertoni permbajtjen per te cilin doni te krijoi nje QRcode: ')
    img = qrcode.make(content)
    img.save(filename + '.png')

def run():
    content = input('Vendosni permbajtjen per te cilen doni te krijoni nje QRcode: ')
    image_qr(content)
    print('QRcode-i juaj eshte krijuar')

if __name__ == '__main__':
    run()