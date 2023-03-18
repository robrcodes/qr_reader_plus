import qrcode

url_data = 'https://github.com/robrcodes'

img_file = 'website_qr.png'

img_qr = qrcode.make(url_data)

img_qr.save(img_file)

