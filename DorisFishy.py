from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

G = [0, 140, 100] #rgb green
P = [150, 15, 140]#rgb purple
B = [0, 20, 120]#rgb blue

Fish1 = [
B, B, B, B, B, B, B, B,
B, B, B, B, B, G, G, B,
B, B, B, G, G, G, B, B,
B, B, B, P, P, P, B, G,
B, B, P, P, P, P, P, B,
B, B, B, B, G, G, B, G,
B, B, B, B, B, B, B, B,
B, B, B, B, B, B, B, B
]

Fish2 = [
B, B, B, B, B, B, B, B,
B, B, B, B, G, G, B, B,
B, B, G, G, G, B, B, B,
B, B, P, P, P, B, G, B,
B, P, P, P, P, P, B, B,
B, B, B, G, G, B, G, B,
B, B, B, B, B, B, B, B,
B, B, B, B, B, B, B, B
]

Fish3 = [
B, B, B, B, B, B, B, B,
B, B, B, G, G, B, B, B,
B, G, G, G, B, B, B, B,
B, P, P, P, B, G, B, B,
P, P, P, P, P, B, B, B,
B, B, G, G, B, G, B, B,
B, B, B, B, B, B, B, B,
B, B, B, B, B, B, B, B
]

Fish4 = [
B, B, B, B, B, B, B, B,
B, B, G, G, B, B, B, B,
G, G, G, B, B, B, B, B,
P, P, P, B, G, B, B, B,
P, P, P, P, B, B, B, P,
B, G, G, B, G, B, B, B,
B, B, B, B, B, B, B, B,
B, B, B, B, B, B, B, B,
]

Fish5 = [
B, B, B, B, B, B, B, B,
B, G, G, B, B, B, B, B,
G, G, B, B, B, B, B, G,
P, P, B, G, B, B, B, P,
P, P, P, B, B, B, P, P,
G, G, B, G, B, B, B, B,
B, B, B, B, B, B, B, B,
B, B, B, B, B, B, B, B,
]

Fish6 = [
B, B, B, B, B, B, B, B,
G, G, B, B, B, B, B, B,
G, B, B, B, B, B, G, G,
P, B, G, B, B, B, P, P,
P, P, B, B, B, P, P, P,
G, B, G, B, B, B, B, G,
B, B, B, B, B, B, B, B,
B, B, B, B, B, B, B, B,
]

Fish7 = [
B, B, B, B, B, B, B, B,
G, B, B, B, B, B, B, G,
B, B, B, B, B, G, G, G,
B, G, B, B, B, P, P, P,
P, B, B, B, P, P, P, P,
B, G, B, B, B, B, G, G,
B, B, B, B, B, B, B, B,
B, B, B, B, B, B, B, B,
]

Fish8 = [
B, B, B, B, B, B, B, B,
B, B, B, B, B, B, G, G,
B, B, B, B, G, G, G, B,
G, B, B, B, P, P, P, B,
B, B, B, P, P, P, P, P,
G, B, B, B, B, G, G, B,
B, B, B, B, B, B, B, B,
B, B, B, B, B, B, B, B,
]


while True:
    sense.set_pixels(Fish1)
    sleep(1)
    sense.set_pixels(Fish2)
    sleep(1)
    sense.set_pixels(Fish3)
    sleep(1)
    sense.set_pixels(Fish4)
    sleep(1)
    sense.set_pixels(Fish5)
    sleep(1)
    sense.set_pixels(Fish6)
    sleep(1)
    sense.set_pixels(Fish7)
    sleep(1)
    sense.set_pixels(Fish8)
    sleep(1)
