
def skytale_encode(input, diameter):
    input = str(input)
    out = str()

    for y in range(0,diameter):
        out += input[y::diameter]

    return out

def skytale_decode(input, diameter):
    pass