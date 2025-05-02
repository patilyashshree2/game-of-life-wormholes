import numpy as np
from collections import defaultdict
from typing import Dict, Tuple

class WormholeMap:
    """
    Builds a bidirectional map from colored wormhole endpoints in a tunnel bitmap.
    Each unique non-black RGB color connects exactly two grid coordinates.
    """

    def __init__(self, tunnel_img: np.ndarray):
        """
        :param tunnel_img: NumPy array of shape (H, W, 3), RGB image
        """
        self.map = self._build_map(tunnel_img)

    def _build_map(self, img: np.ndarray):
        color_to_coords = defaultdict(list)

        for y in range(img.shape[0]):
            for x in range(img.shape[1]):
                color = tuple(img[y, x])
                if color != (0, 0, 0):  # skip black
                    color_to_coords[color].append((y, x))

        wormhole_map = {}
        for coords in color_to_coords.values():
            if len(coords) == 2:
                a, b = coords
                wormhole_map[a] = b
                wormhole_map[b] = a

        return wormhole_map
