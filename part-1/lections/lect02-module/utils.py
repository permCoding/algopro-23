def to_int(b):
    dec = 0
    for i in range(len(b)):
        dec += int(b[i]) * 2**(len(b)-1-i)
    return dec


def to_int_(b):
    dec = 0
    for i in range(len(b)):
        if b[i] == "0":
            value = 0
        else: 
            value = 1
        dec += value * 2**(len(b)-1-i)
    return dec


def to_int__(b):
    dec = 0
    for i in range(len(b)):
        value = 0 if b[i] == "0" else 1
        dec += value * 2**(len(b)-1-i)
    return dec
