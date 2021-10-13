import qrcode
import random

def generate_password(n_characters):
    lower = 'abcdefhijklmnopqrstuvxyz'
    upper = 'ABCDEFHIJKLMNOPQRSTUVXYZ'
    numbers = '12345678901234567890'
    symbols = '!"#$%&/()={}[]'
    all_characters = lower + upper + numbers + symbols

    password = ''.join(random.sample(all_characters, n_characters))

    return password

def image_qr(password):
    filename = input('Emertoni Passwordin tuaj: ')
    img = qrcode.make(password)
    img.save(filename + '.png')

def run():
    characters = int(input('Numri i karaktereve: '))
    password = generate_password(characters)
    print(f'Passwordi juaj i ri eshte: {password}')
    image_qr(password)
    print('Passwordi eshte ruajtur si nje imazhe QR Code')

if __name__ == '__main__':
    run()