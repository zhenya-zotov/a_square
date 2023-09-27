def is_square(n):    
    from math import sqrt

    if n < 0:
        return False
    elif sqrt(n) % 1 == 0:
        return True
    else:
        return False
