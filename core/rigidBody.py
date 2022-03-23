from math import dist
import numpy as np
from physics import *
from shapes import *

class rigidBody:

    position: vector2 = vector2()
    velocity: vector2 = vector2()
    rotation: float = 0.0
    rotational_velocity: float = 0.0

    acceleration: vector2 = vector2()
    rotational_acceleration: float = 0.0

    mass: float = 1.0
    moment_of_inertia: float = 1.0
    
    is_static: bool = True
    elastic_coeff: float = 1.0

    is_elastic: bool = False


    def __init__(self, shape: rPolygon, position: vector2 = vector2(), velocity: vector2 = vector2(), mass: float = 1.0, moment_of_inertia: float = 1.0, is_static: bool = False, elastic_coeff: float = 1.0):
        
        self.position = position
        self.velocity = velocity
        self.rotation = shape.rotation
        self.rotational_velocity = 0.0

        self.acceleration = vector2()
        self.rotational_acceleration = 0.0

        self.shape = shape

        self.mass: float = mass
        self.moment_of_inertia: float = moment_of_inertia

        self.is_static = is_static

        self.is_elastic = True
        self.elastic_coeff = elastic_coeff

    def apply_force(self, force: vector2, point: vector2):

        acc = force / self.mass
        self.acceleration += acc

        self.rotational_acceleration += (point - self.position).cross(force) / self.moment_of_inertia

    def apply_force_local(self, force: vector2, point: vector2):

        acc = force / self.mass
        self.acceleration += acc

        self.rotational_acceleration += (point.cross(force)) / self.moment_of_inertia

    def check_collisions(self, objects: list[rPolygon]):

        for obj in objects:
            
            distance = (obj.position - self.position).magnitude()
            # check if we are able to collide with the object
            if distance < obj.shape.radius + self.shape.radius:

                smallest_dist = distance
                closest_vert = 0
                for idx, vertex in enumerate(self.shape.vertices):

                    vert_dist = (obj.position - (vertex + self.position)).magnitude() - obj.shape.radius

                    if vert_dist < smallest_dist:
                        smallest_dist = vert_dist
                        closest_vert = idx

                closest_other_vert = 0
                closest_other_dist = distance
                for idx, vertex in enumerate(obj.shape.vertices):

                    vert_dist = ((self.position + self.shape.vertices[closest_vert]) - (vertex + obj.position)).magnitude() - self.shape.radius

                    if vert_dist < closest_other_dist:
                        closest_other_dist = vert_dist
                        closest_other_vert = idx

                vert_dist_1 = ((self.position + self.shape.vertices[closest_vert+1]) - (obj.shape.vertices[closest_other_vert] + obj.position)).magnitude() - self.shape.radius
                vert_dist_2 = ((self.position + self.shape.vertices[closest_vert-1]) - (obj.shape.vertices[closest_other_vert] + obj.position)).magnitude() - self.shape.radius

                if vert_dist_1 < vert_dist_2:
                    second_vert = closest_vert + 1
                else:
                    second_vert = closest_vert - 1
                
                distance_between_verts = self.shape.vertices[second_vert] - self.shape.vertices[closest_vert]

                dist_slope = distance_between_verts.y / distance_between_verts.x
                dist_intercept = self.shape.vertices[closest_vert].y - dist_slope * self.shape.vertices[closest_vert].x

                object_collision_pos = vector2(obj.shape.vertices[closest_other_vert].x, dist_slope*obj.shape.vertices[closest_other_vert].x + dist_intercept)

                vFinal = ((self.velocity * (self.mass - obj.mass)) + (obj.velocity * obj.mass) * 2) / (self.mass + obj.mass)

                # print(f"velocity change: {velocity_change}")
                self.apply_force((self.velocity*-self.mass/0.01)+(vFinal*self.mass)/0.01, object_collision_pos)

    def update(self, dt: float):
        if not self.is_static:
            self.velocity += self.acceleration * dt
            self.position += (self.velocity * dt) 
            

            self.rotation += self.rotational_velocity * dt + (0.5 * self.rotational_acceleration * dt * dt)
            self.rotational_velocity += self.rotational_acceleration * dt

            self.shape.set_rotation(self.rotation)

            self.rotational_acceleration = 0.0
            self.acceleration = vector2(0.0, 0.0)
