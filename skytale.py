
import math

def skytale_encode(input, diameter):
    input = str(input)
    out = str()

    for y in range(0,diameter):
        out += input[y::diameter]

    return out

def skytale_decode(input, diameter):
    input = str(input)
    diameter = math.ceil(len(input)/2)
    out = str()

    for y in range(0,diameter):
        out += input[y::diameter]
    return out
