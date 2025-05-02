import numpy as np
from models.wormhole_map import WormholeMap


class GameEngine:
    """
    Simulates Conway's Game of Life with optional wormhole-enhanced neighbor logic.
    """

    def __init__(self, initial_grid: np.ndarray, h_wormholes: WormholeMap, v_wormholes: WormholeMap):
        self.grid = initial_grid  # binary 2D numpy array
        self.h_wormholes = h_wormholes.map
        self.v_wormholes = v_wormholes.map
        self.height, self.width = self.grid.shape
        self.count_live = []

    def get_neighbors(self, y: int, x: int):
        """
        Returns coordinates of neighboring cells considering wormhole remapping.
        """
        directions = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1)
        ]

        neighbors = []

        for dy, dx in directions:
            # Step 1: wormhole redirection from source cell (y, x)
            if dy == -1 and dx == 0 and (y, x) in self.v_wormholes:
                base = self.v_wormholes[(y, x)]
                ny, nx = base[0] - 1, base[1]
            elif dy == 1 and dx == 0 and (y, x) in self.v_wormholes:
                base = self.v_wormholes[(y, x)]
                ny, nx = base[0] + 1, base[1]
            elif dy == 0 and dx == 1 and (y, x) in self.h_wormholes:
                base = self.h_wormholes[(y, x)]
                ny, nx = base[0], base[1] + 1
            elif dy == 0 and dx == -1 and (y, x) in self.h_wormholes:
                base = self.h_wormholes[(y, x)]
                ny, nx = base[0], base[1] - 1
            elif dy != 0 and dx != 0:
                if dy == -1 and (y, x) in self.v_wormholes:
                    base = self.v_wormholes[(y, x)]
                    ny, nx = base[0] - 1, base[1] + dx
                elif dx == 1 and (y, x) in self.h_wormholes:
                    base = self.h_wormholes[(y, x)]
                    ny, nx = base[0] + dy, base[1] + 1
                elif dy == 1 and (y, x) in self.v_wormholes:
                    base = self.v_wormholes[(y, x)]
                    ny, nx = base[0] + 1, base[1] + dx
                elif dx == -1 and (y, x) in self.h_wormholes:
                    base = self.h_wormholes[(y, x)]
                    ny, nx = base[0] + dy, base[1] - 1
                else:
                    ny, nx = y + dy, x + dx
            else:
                ny, nx = y + dy, x + dx

            # Step 2: re-apply direction from remapped destination
            if (ny, nx) in self.v_wormholes:
                base = self.v_wormholes[(ny, nx)]
                ny, nx = base[0] + dy, base[1] + dx
            elif (ny, nx) in self.h_wormholes:
                base = self.h_wormholes[(ny, nx)]
                ny, nx = base[0] + dy, base[1] + dx

            if 0 <= ny < self.height and 0 <= nx < self.width:
                neighbors.append((ny, nx))

        return neighbors

    def step(self):
        """
        Performs a single step of the Game of Life using wormhole-enhanced topology.
        """
        new_grid = self.grid.copy()
        for y in range(self.height):
            for x in range(self.width):
                live_neighbors = sum(self.grid[ny, nx] for ny, nx in self.get_neighbors(y, x))
                if self.grid[y, x] == 1:
                    new_grid[y, x] = 1 if live_neighbors in [2, 3] else 0
                else:
                    new_grid[y, x] = 1 if live_neighbors == 3 else 0
        self.grid = new_grid



    def run(self, steps: int) -> np.ndarray:
        """
        Executes the simulation for the given number of steps.
        """
        for step in range(steps):
            self.step()
            # if _ == steps-1:
            #     for y in range(self.height):
            #         for x in range(self.width):
            #             if self.grid[y][x] == 1:
            #                 self.count_live.append([y, x])

        # print(self.count_live)
        # print("I am here")
        return self.grid

    


    