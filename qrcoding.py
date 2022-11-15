import qrcode
import image

qt=qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)

Data1="www.linkedin.com/in/tanushree-sahu-090523220"

qt.add_data(Data1)
qt.make(fit=True)
img=qt.make_image(fill_color="black", back_color="white")
img.save("my_linkedin.png")