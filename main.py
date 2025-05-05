import pygame
import trans
import donut

DONUT_QUALITY = 15 # this scales very fast

WIDTH, HEIGHT = 600, 600

WIN = pygame.display.set_mode((WIDTH, HEIGHT))


BGCOLOR = (50, 54, 61)

CAMERA_SPEED = 2
env = trans.Environment(90)
env.set_camera(trans.Vector3(0, 0, -100))

torus = donut.Donut(DONUT_QUALITY, 20, 40)
env.add_child(torus)
"""
vertex1 = trans.Vertex(trans.Vector3(0, 0, 75))
vertex2 = trans.Vertex(trans.Vector3(50, 0, 100))
vertex3 = trans.Vertex(trans.Vector3(-25, 0, 100))

triangle = trans.Triangle(vertex1, vertex2, vertex3)
env.add_child(triangle)

vertex2 = trans.Vertex(trans.Vector3(0, 0, 75))
vertex1 = trans.Vertex(trans.Vector3(0, 25, 100))
vertex3 = trans.Vertex(trans.Vector3(-25, 0, 100))

triangle = trans.Triangle(vertex1, vertex2, vertex3)
env.add_child(triangle)


vertex1 = trans.Vertex(trans.Vector3(0, 0, 75))
vertex2 = trans.Vertex(trans.Vector3(0, 25, 100))
vertex3 = trans.Vertex(trans.Vector3(50, 0, 100))

triangle = trans.Triangle(vertex1, vertex2, vertex3)
env.add_child(triangle)

vertex2 = trans.Vertex(trans.Vector3(-25, 0, 100))
vertex1 = trans.Vertex(trans.Vector3(0, 25, 100))
vertex3 = trans.Vertex(trans.Vector3(50, 0, 100))

triangle = trans.Triangle(vertex1, vertex2, vertex3)
env.add_child(triangle)
"""
# brown thing at the bottom
vertex1 = trans.Vertex(trans.Vector3(-100, -50, -100))
vertex2 = trans.Vertex(trans.Vector3(-100, -50, 100))
vertex3 = trans.Vertex(trans.Vector3(100, -50, 100))

triangle = trans.Triangle(vertex1, vertex2, vertex3, (139,69,19))
env.add_child(triangle)


vertex1 = trans.Vertex(trans.Vector3(-100, -50, -100))
vertex2 = trans.Vertex(trans.Vector3(100, -50, 100))
vertex3 = trans.Vertex(trans.Vector3(100, -50, -100))

triangle = trans.Triangle(vertex1, vertex2, vertex3, (139,69,19))
env.add_child(triangle)
def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()


def handle_input():
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        env.move_camera(trans.Vector3(0, 0, -CAMERA_SPEED))

    if keys[pygame.K_s]:
        env.move_camera(trans.Vector3(0, 0, CAMERA_SPEED))

    if keys[pygame.K_d]:
        env.move_camera(trans.Vector3(-CAMERA_SPEED, 0, 0))

    if keys[pygame.K_a]:
        env.move_camera(trans.Vector3(CAMERA_SPEED, 0, 0))

    if keys[pygame.K_q]:
        env.move_camera(trans.Vector3(0, CAMERA_SPEED, 0))

    if keys[pygame.K_e]:
        env.move_camera(trans.Vector3(0, -CAMERA_SPEED, 0))

    if keys[pygame.K_LEFT]:
        env.rotate_camera(trans.Vector3(0, -CAMERA_SPEED, 0))

    if keys[pygame.K_RIGHT]:
        env.rotate_camera(trans.Vector3(0, CAMERA_SPEED, 0))


def draw():
    WIN.fill(BGCOLOR)

    env.display(WIN)

    pygame.display.update()


def main():


    clock = pygame.time.Clock()
    while True:
        clock.tick(60)

        handle_events()

        handle_input()

        draw()


if __name__ == "__main__":
    main()
