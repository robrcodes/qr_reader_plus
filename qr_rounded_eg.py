import qrcode

from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer

url_data = 'https://github.com/robrcodes'

img_file = '3website_qr.png'

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
qr.add_data(url_data)

img_1 = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())

img_1.save(img_file)

# This code directly take from:
# https://github.com/lincolnloop/python-qrcode
