# InputValidator.py
# Contributors: Ben

# `callback` is an optional parameter
# That's what the `*` means

# Usage:
# input_float(<text you want to print out>)
# OR you could add a second parameter; It's an optional parameter
# input_float(<text>, <text you want to print out WHEN the input is invalid>)

def input_float(text : String, *callback) -> float:
    i = (input(text))
    while type(i) != float:
        try:
            i = float(i)
        except:
            i = (input(text))
            if callback:
#               `[0]` is only because the `*` sets `callback` to a Tuple instead of a String
#               I have no idea why it does this
                print(callback[0])
    else:
        return float(i)

def input_int(text : String, *callback) -> int:
    i = (input(text))
    while type(i) != int:
        try:
            i = float(i)
            i = int(i)
        except:
            i = (input(text))
            if callback:
                print(callback[0])
    else:
        return int(i)

def input_str(text : str, *callback) -> str:
    i = (input(text))
    while type(i) != str:
        try:
            i = str(i)
        except:
            i = (input(text))
            if callback:
                print(callback[0])
    else:
        return str(i)