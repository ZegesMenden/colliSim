from __future__ import annotations
from dataclasses import dataclass
import numpy as np

DEG_TO_RAD = np.pi / 180.0
RAD_TO_DEG = 180 / np.pi

@dataclass
class vector2:

    x: float = 0.0
    y: float = 0.0

    def __init__(self, x: float = 0.0, y: float = 0.0) -> vector2:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return(f'{self.x}, {self.y}')

    def __add__(self, other) -> vector2:

        if isinstance(other, vector2):
            return vector2(self.x + other.x, self.y + other.y)
        else:
            raise NotImplementedError

    def __sub__(self, other) -> vector2:

        if isinstance(other, vector2):
            return vector2(self.x - other.x, self.y - other.y)
        else:
            raise NotImplementedError

    def __mul__(self, other) -> vector2:

        if isinstance(other, vector2):
            return vector2(self.x * other.x, self.y * other.y)
        else:
            if isinstance(other, float) or isinstance(other, int):
                return vector2(self.x * other, self.y * other)
            else:
                raise NotImplementedError
    
    def __truediv__(self, other) -> vector2:

        if isinstance(other, vector2):
            return vector2(self.x / other.x, self.y / other.y)
        else:
            if isinstance(other, float) or isinstance(other, int):
                return vector2(self.x / other, self.y / other)
            else:
                raise NotImplementedError

    def magnitude(self) -> float:
        return np.sqrt(self.x*self.x + self.y*self.y)

    def norm(self) -> vector2:
        return self / self.magnitude()

    def cross(self, other: vector2) -> float:
        return (self.x*other.y) - (self.y*other.x)

def rotate_vector_around_point(vec: vector2, rotation: float, point: vector2 = vector2(0, 0)) -> vector2:
    tmp: vector2 = vec - point
    return vector2((tmp.x * np.cos(rotation) - tmp.y * np.sin(rotation)) + point.x, (tmp.x * np.sin(rotation) + tmp.y * np.cos(rotation)) + point.y)
