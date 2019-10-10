import collections
Point = collections.namedtuple("Point", "x y")

class MoveException(Exception):
    pass