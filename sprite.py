import time
import machine
import neopixel

pixelcount = 85
np = NeoPixel(machine.Pin(4), pixelcount, brightness=1.0)
for n in range(pixelcount):
    np[n] = (0, 0, 0)
np.write()
pumpkin = 'ooooooooog'
ghost = 'wwwwnnwwnnwwww'
vampire = 'vvvvrrvvrrvvvvv'

colors = {
    'o': (255,69,0),
    'g': (0,255,0),
    'w': (255,255,255),
    'n': (0,0,0),
    'v': (255,0,255),
    'r': (255,0,0)
}
sprites = [ { 'sprite': pumpkin, 'position': -10, 'speed': 2 }, { 'sprite': ghost, 'position': -50, 'speed': 2 },
            { 'sprite': vampire, 'position': -80, 'speed': 2 }]

while True:
    for n in range(pixelcount):
        np[n] = (0, 0, 0)
    #draw sprites
    for sprite in sprites:
        sprite['position'] = sprite['position'] + sprite['speed']
        if sprite['position'] > pixelcount + len(sprite['sprite']):
            sprite['position'] = len(sprite['sprite'])
        for idx, pixel in enumerate(sprite['sprite']):
            if sprite['position'] + idx < pixelcount - 1:
                np[sprite['position'] + idx] = colors[pixel]
            else:
                np[(sprite['position'] + idx) - pixelcount] = colors[pixel]
    np.write()
