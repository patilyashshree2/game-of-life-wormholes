from PIL import Image
import numpy as np
from fastapi import UploadFile
import io


class ImageLoader:
    """
    Factory class to load and convert image files into NumPy arrays.
    """

    @staticmethod
    def load_grayscale_image(file: UploadFile) -> np.ndarray:
        """
        Loads a PNG and returns a 2D binary (0 or 1) array based on luminance.
        """
        image = Image.open(io.BytesIO(file.file.read())).convert("L")
        array = np.array(image)
        return (array > 127).astype(np.uint8)  # binary: 0 or 1

    @staticmethod
    def load_rgb_image(file: UploadFile) -> np.ndarray:
        """
        Loads a PNG and returns a 3D RGB array (H, W, 3).
        """
        image = Image.open(io.BytesIO(file.file.read())).convert("RGB")
        return np.array(image)
