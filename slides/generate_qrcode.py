import qrcode

qr = qrcode.QRCode()
qr.add_data("https://arxiv.org/abs/2102.08649")
qr.make()
img = qr.make_image(fill_color=(255, 255, 255), back_color=(38, 62, 66))
img.save("figures/qrcode_slides.png")

img = qr.make_image(fill_color=(0, 0, 0), back_color=(255, 255, 255))
img.save("figures/qrcode_poster.png")
