
def skytale_encode(input, diameter):
    out = str()
    for y in range(0,diameter):
        out += input[y::diameter]
    return out
