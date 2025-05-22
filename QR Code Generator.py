import PIL;
from PIL import Image;

import qrcode;
from qrcode.image.styledpil import StyledPilImage;
from qrcode.image.styles.moduledrawers import VerticalBarsDrawer;
from qrcode.image.styles.colormasks import SolidFillColorMask;

#Referência de fazeção - https://github.com/reegan-anne/python_qrcode/blob/main/main.ipynb

if not hasattr(PIL.Image, 'Resampling'):
  PIL.Image.Resampling = PIL.Image
# Now PIL.Image.Resampling.BICUBIC is always recognized.



#Seleciona a imagem que eu quero usar de centro
logo = 'assets/cachirro.jpg';

#Coloca as opções de personalização do qrcode em si
qr = qrcode.QRCode(
        version = 5, #Pelo que entendi é o tanto de repetições que acontece
        error_correction = qrcode.constants.ERROR_CORRECT_H, #É o tanto de dano que ele pode tomar até ficar ilegível
        border = 2 #Borda ao redor do QR Code
);

#Informação que eu quero transformar em qr code
qr.add_data('https://www.instagram.com/gruposansey?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==')

#Faz a imagem em si, colocando junto as personalizações que eu quero
qr_img = qr.make_image(image_factory = StyledPilImage,
                       module_drawer = VerticalBarsDrawer(), #Ele escolhe o jeito que as barras vão ser
                       color_mask = SolidFillColorMask(front_color=(218, 3, 2), back_color=(255, 255, 255)), #Cores
                       embeded_image_path = logo #Imagem que fica no centro
                       );

#Salva a imagem
qr_img.save('Testando2.png');
