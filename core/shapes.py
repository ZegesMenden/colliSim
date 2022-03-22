import numpy as np
from core.physics import *

def init_polygon_vertex_positions(sides: int = 3, radius: float = 1.0):
    ret = []
    for i in range(sides):
        ret.append(vector2(radius * np.cos(2 * np.PI * i / sides), radius * np.sin(2 * np.PI * i / sides)))
    return ret

class polygon:

    sides: list = []
    rotation: float = 0.0

    def __init__(self, sides: list, radius: float = 1.0, rotation: float = 0.0):

        self.sides = init_polygon_vertex_positions(sides, radius)
        