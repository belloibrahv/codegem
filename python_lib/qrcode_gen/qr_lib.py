import qrcode
from PIL import Image


class QRCodeGenarator:
    def __init__(self, version=1, box_size=10, border=5):
        '''
        Initialize the QR code generator with optional configuration.
        :param version: Controls the size of the QR Code (1 to 40).
        :param box_size: Size of the box where QR Code pixel are drawn.
        :border: Thickness of the border.
        '''
        self.version = version
        self.box_size = box_size
        self.border = border
        
    
    def generate_qr(self, data, file_path=None, fill_color='black', back_color='white'):
        '''
        Generate QR code from provided data and save it to the path (if provided).
        :param data: The information to encode the QR code (eg., URL or text).
        :param file_path: The path to save generated QR code image (Optional).
        :param fill_color: Color of the QR code.
        :param back_color: Background color of the QR code.
        :return: QR code image object. 
        '''
        qr = qrcode.QRCode(
            border=self.border,
            version=self.version,
            box_size=self.box_size,
            error_correction=qrcode.ERROR_CORRECT_L
        )
        qr.add_data(data)
        qr.make(fit=True)
        
        img = qr.make_image(file_path=file_path, back_color=back_color)
        
        if file_path:
            img.save(file_path)
            print(f'QR code saved as {file_path}')
            
        return img
          
        
    def display_qr(self, data, fill_color='black', back_color='white'):
        '''
        Display generated QR code without saving it to disk.
        :param file_path: The path to save generated QR code image (Optional).
        :param fill_color: Color of the QR code.
        :param back_color: Background color of the QR code.
        '''
        img = self.generate_qr(data=data, fill_color=fill_color, back_color=back_color)
        img.show()
    