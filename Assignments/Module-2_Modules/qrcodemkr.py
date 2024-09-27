"""import pyqrcode

url="https://www.tops-int.com/"

qr=pyqrcode.create(url)

qr.png("tops.png")"""


import qrcode

#url="https://www.tops-int.com/"

url="Hello Students, Welcome to TOPS!"

qr=qrcode.make(url)

qr.save('test.png')