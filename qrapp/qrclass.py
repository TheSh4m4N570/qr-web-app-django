import json

import qrcode.constants
from qrcode import QRCode
from pathlib import Path
from .qrclassconfig import config
import logging


class ProductQr:
    DATA_SAVED = Path.cwd() / "qrs"

    def __init__(self, qr_url):
        self.qr_url = qr_url

    def __str__(self):
        return self.qr_url

    def _get_product(self):
        return self.qr_url

    def generate_qr_image(self):
        url_to_convert = self._get_product()
        qr = QRCode(
            version=config.VERSION,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=config.BOX_SIZE,
            border=config.BORDER
        )
        qr.add_data(url_to_convert)
        qr.make(fit=True)
        img = qr.make_image(fill_color=config.DEFAULT_FILL_COLOR, back_color=config.DEFAULT_BG_COLOR)
        return img


    def save_image_to(self):
        img = self.generate_qr_image()
        folder = self.DATA_SAVED / self.country
        folder.mkdir(parents=True, exist_ok=True)
        img.save(f"{folder}/{self.product}.png")


if __name__ == "__main__":
    pass