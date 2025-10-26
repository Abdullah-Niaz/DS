import numpy as np


def slope(x1, x2, y1, y2):
    """
        This function takes the parameter of the line and calculates the slope of the line
    """
    s = (y2 - y1) / x2 - x1
    return s


a = slope(2, 3, 4, 5)
print(f"Slope {a}")
print(slope.__doc__)
print(np.mean.__doc__)
