import cv2
import numpy as np


def second_norm(x1, x2):
    """
    calculates second norm of difference of two vectors, also called euclidian norm
    :param x1: first vector
    :param x2: second vector
    :return: second norm of vector x1-x2
    """
    return np.sqrt(np.sum((np.asarray(x1) - np.asarray(x2)) ** 2))


def not_same_color(x1, x2):
    return second_norm(x1, x2) >= 15


def same_color(x1, x2):
    return not (not_same_color(x1, x2))


def count_percentage(image):
    height = image.shape[0]
    width = image.shape[1]
    glass_pixels = 0
    glass_dimensions = []
    for y in range(0, height):
        x_to_remember = -1
        x_finished_at = -1

        for x in range(width - 1):

            if not_same_color(image[y][x], image[y][x - 1]):
                x_to_remember = x
                break

        for x in range(width - 2, 0, -1):
            if not_same_color(image[y][x], image[y][x + 1]):
                x_finished_at = x
                break

        glass_pixels += (x_finished_at - x_to_remember)

        glass_dimensions.append([y, x_to_remember, x_finished_at])

    liquid_pixels = 0

    coffee = 0
    tea = 0
    water = 0
    for row in glass_dimensions:

        background = []
        for x in range(row[1]):
            background.append(image[row[0]][x])
        inside_glass = []
        for x in range(row[1], row[2]):
            inside_glass.append(image[row[0]][x])

        background = list(map(lambda rgb: sum(list(rgb)) / 3, background))
        inside_glass = list(map(lambda rgb: sum(list(rgb)) / 3, inside_glass))
        back_color = np.mean(background)
        inside_color = np.mean(inside_glass)

        if abs(back_color - inside_color >= 70):
            liquid_pixels += row[2] - row[1]

            if inside_color < 130:
                coffee += row[2] - row[1]
            elif inside_color < 150:
                tea += row[2] - row[1]
            else:
                water += row[2] - row[1]

    water = 100 * (water / liquid_pixels)
    coffee = 100 * (coffee / liquid_pixels)
    tea = 100 * (tea / liquid_pixels)

    print(f"Water:{water},coffee:{coffee}, tea:{tea} ")
    return 100 * (liquid_pixels / glass_pixels)


cap = cv2.VideoCapture('../test/circle.mp4')

n = 0
while True:
    try:
        _, frame = cap.read()
        print('at frame', n)
        print(count_percentage(frame), '%')
        n += 1
        cv2.imshow('press d to exit', frame)
        if cv2.waitKey(20) & 0xFF == ord('d'):
            break
    except:
        break
