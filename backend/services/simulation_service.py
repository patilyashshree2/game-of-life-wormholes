from typing import List, Dict
from fastapi import UploadFile
from models.image_loader import ImageLoader
from models.wormhole_map import WormholeMap
from models.game_engine import GameEngine


class SimulationService:
    """
    Coordinates the simulation pipeline: image decoding, wormhole mapping, and execution.
    """

    def __init__(self):
        self.loader = ImageLoader()

    async def run_all_iterations(
        self,
        start_img: UploadFile,
        h_tunnel: UploadFile,
        v_tunnel: UploadFile,
        iterations: List[int]
    ) -> Dict[int, 'np.ndarray']:
        """
        Runs multiple iteration counts on a Game of Life board with wormholes.
        :return: Dictionary mapping iteration count to the resulting grid.
        """
        # Load image data
        grid = self.loader.load_grayscale_image(start_img)
        h_img = self.loader.load_rgb_image(h_tunnel)
        v_img = self.loader.load_rgb_image(v_tunnel)

        # Build wormhole maps
        h_map = WormholeMap(h_img)
        v_map = WormholeMap(v_img)

        # Run separate engine instance per iteration to isolate mutations
        results = {}
        for step in iterations:
            engine = GameEngine(grid.copy(), h_map, v_map)
            results[step] = engine.run(step)
            

        return results
