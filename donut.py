import trans
import pygame
import random

ROTATION_SPEED = trans.Vector3(0.1, 0.5, 0.25)

colors = [
    *([(255, 0, 255)] * 10),
    (255, 0, 0),     # Red
    (0, 0, 255),     # Blue
    (0, 255, 0),     # Green
    (255, 255, 0),   # Yellow
    (128, 0, 128),   # Purple
    (255, 165, 0),   # Orange
]
def choose_color(y):
    if y > 3:
        return random.choice(colors)
    else: return (139,69,19)

class Donut:
    def __init__(self, quality: int, r: int, R: int):
        self.points = []
        self.triangles = []

        self.generate_torus(quality, r, R)
        self.rotation_vect = trans.Vector3(0, 0, 0)

    def generate_torus(self, quality, r, R):
        self.points = []

        circle = []
        right_vector = trans.Vector3(1, 0, 0)
        distance = 360 / quality
        for i in range(quality):
            circle.append(right_vector.rotate(trans.Vector3(0, 0, i * distance)) * r)

        for i in range(quality * 2 + 1):
            rotation_vector = trans.Vector3(0, i * distance / 2, 0)
            center = right_vector.rotate(rotation_vector) * R

            section = []
            for point in circle:
                section.append(trans.Vertex(point.rotate(trans.Vector3(0, 0, distance / 2 * (i % 2))).rotate(rotation_vector) + center))

            k = 0
            while k < len(section) and i != 0:
                v1, v2 = section[k], section[(k + 1) % len(section)]
                v3 = self.points[-len(section) + (k + (i % 2)) % len(section)]
                v4 = self.points[-len(section) + (k - 1 + (i % 2)) % len(section)]

                color = choose_color(sum([vert.position.y for vert in (v1, v2, v3)]) / 4)
                self.triangles.append(trans.Triangle(v1, v2, v3, color))
                color = (255, 0, 255) if sum([vert.position.y for vert in (v1, v4, v3)]) / 4 > 3 else (139,69,19)
                self.triangles.append(trans.Triangle(v1, v3, v4, color))
                k += 1

            self.points.extend(section)
        print(len(self.triangles))

    def distance_from_camera(self, *args, **kwargs):
        return 0

    def display(self, surface: pygame.Surface, offset: trans.Vector3, rotation: trans.Vector3, FOV: int):
        copy = [i.position for i in self.points]

        for point in self.points:
            point.position = point.position.rotate(self.rotation_vect)

        self.rotation_vect = self.rotation_vect + ROTATION_SPEED
        self.rotation_vect.x %= 360
        self.rotation_vect.y %= 360
        self.rotation_vect.z %= 360

        for i in sorted(self.triangles, key = (lambda x: x.distance_from_camera(offset)), reverse=False):
            i.display(surface, offset, rotation, FOV)

        for i, point in enumerate(self.points):
            self.points[i].position = copy[i]
