"""
class T:

    def __init__(self , phi: list):
        self.phi = phi


class S(T):
    pass


if __name__ == "__main__":
    x = T(phi=[ "a" , "b" ])
    y = S(phi=[ "c" , "d" ])
"""

"""
class T:

    def __init__(self , phi: list):
        self.phi = phi


class S(T):

    def __init__(self , phi: str):
        self.phi = phi


if __name__ == "__main__":
    x = T(phi=[ "a" , "b" ])
    y = S(phi="c, d")
"""