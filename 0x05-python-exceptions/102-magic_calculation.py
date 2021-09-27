def magic_calculation(a, b):
    var = 0
    for i in range(1, 3):
        try:
            if (i > a):
                raise Exception('Too far')
            else:
                var += (a**b)/i
        except:
            var = (b + a)
            break
    return var
