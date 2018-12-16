'''
Each day a plant is growing by upSpeed meters. Each night that plant's height decreases by downSpeed meters due to the lack of sun heat. Initially, plant is 0 meters tall. We plant the seed at the beginning of a day. We want to know when the height of the plant will reach a certain level.

Example
For upSpeed = 100, downSpeed = 10 and desiredHeight = 910, the output should be 10.
'''


def growing_plant(u, d, H):
    h = 0
    x = 0
    while h < H or H == 0:
        h = h + u
        x += 1
        if h >= H:
            break
        h = h - d
    return x
