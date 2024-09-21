import simplestart as ss
import qrcode
from io import BytesIO
from PIL import Image

#api
def generate_qr_code(link):  # Generate QR Code
    qr = qrcode.QRCode(
        version=1.00,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2,
    )
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img


def download_qr_code(img):  # Convert PIL image to bytes
    img_bytes = BytesIO()
    img.save(img_bytes, format='PNG')
    img_bytes.seek(0)
    return img_bytes

#event handler
def text_change(event):
    generate_img()
    
def generate_img():
    link = link_text.value
    qr_img = generate_qr_code(link)
    img = download_qr_code(qr_img)
    myimg.image = img
    
#ui
ss.write("# QR Code Generator")
link_text = ss.text_input("http://www.simplestart.cc", label = "Enter a link:", onchange = text_change, max_width = 600)
myimg = ss.image("", title='Generated QR Code', width=300, border= True)

generate_img()

ss.link("Download QR Code", myimg.image, file_name = "qr_code.png", mime = "image/png")
