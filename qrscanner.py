import qrcode
# import random
from PIL import Image

x = input("Enter the url u want to convert in qr code : ")
n = input("Enter a name for that qr code image: ")

# def select_name(strings):
#     sts = strings.split({"&", "/", "=", "?"})
#     rand_name = random.choice(sts)
#     return rand_name


myqr = qrcode.make(x)
# s = select_name(x)
myqr.save(f"{n}.png", scale=8)
img = Image.open(f'{n}.png')
img.show()
