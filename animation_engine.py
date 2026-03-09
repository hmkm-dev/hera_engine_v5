def pop(txt):
    return txt.resize(lambda t: 1+0.4*t)

def slide(txt):
    return txt.set_position(lambda t: ("center", 800-200*t))

def zoom(txt):
    return txt.resize(lambda t:1+0.2*t)