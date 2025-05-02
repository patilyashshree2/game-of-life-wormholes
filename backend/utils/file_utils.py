from PIL import Image
import numpy as np


def save_image(array: np.ndarray, path: str):
    """
    Saves a binary NumPy array (0/1) as a grayscale PNG.

    :param array: 2D NumPy array of 0s and 1s
    :param path: Output file path
    """
    image = Image.fromarray(array.astype(np.uint8) * 255).convert("L")
    image.save(path)
