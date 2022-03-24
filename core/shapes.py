import numpy as np
from core.physics import *

def init_polygon_vertex_positions(sides: int = 3, radius: float = 1.0):
    ret = []
    for i in range(sides):
        ret.append(vector2(radius * np.cos(2 * np.pi * i / sides), radius * np.sin(2 * np.pi * i / sides)))
    return ret

class rPolygon:
    nVertices: int = 0
    vertices: list = []
    rotation: float = 0.0

    def __init__(self, vertices: list, radius: float = 1.0, rotation: float = 0.0):
        self.radius = radius
        self.nVertices = vertices
        self.vertices = init_polygon_vertex_positions(vertices, radius)
        self.rotaion = rotation
        if rotation != 0.0:
            for vertex in self.vertices:
                vertex = rotate_vector_around_point(vertex, rotation)

    def rotate(self, rotation: float):
        self.rotation += rotation
        for vertex in self.vertices:
            vertex = rotate_vector_around_point(vertex, rotation)

    def set_rotation(self, rotation: float):
        dRot = rotation - self.rotation
        for vertex in self.vertices:
            vertex = rotate_vector_around_point(vertex, dRot)

class square(rPolygon):
    def __init__(self, radius: float = 1.0, rotation: float = 0.0):
        super().__init__(4, radius, rotation)

class triangle(rPolygon):
    def __init__(self, radius: float = 1.0, rotation: float = 0.0):
        super().__init__(3, radius, rotation)

