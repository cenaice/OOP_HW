import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def translate(self, s, t):
        self.x += s
        self.y += t

    def rotate(self, theta):
        x = self.x * math.cos(theta) - self.y * math.sin(theta)
        y = self.x * math.sin(theta) + self.y * math.cos(theta)
        self.x = x
        self.y = y

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx * dx + dy * dy)

    def left_of(self, q, r):
        qr_x = r.x - q.x
        qr_y = r.y - q.y
        ps_x = self.x - q.x
        ps_y = self.y - q.y
        return qr_x * ps_y - qr_y * ps_x > 0

    def right_of(self, q, r):
        qr_x = r.x - q.x
        qr_y = r.y - q.y
        ps_x = self.x - q.x
        ps_y = self.y - q.y
        return qr_x * ps_y - qr_y * ps_x < 0

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

class SimplePoly:
    class SimplePolyIterator:
        def __init__(self, polygon):
            self.polygon = polygon
            self.current = 0
        
        def __next__(self):
            if self.current >= len(self.polygon):
                raise StopIteration
            else:
                result = self.polygon[self.current]
                self.current += 1
                return result
    
    def __init__(self, *vertices):
        self.vertices = list(vertices)
    
    def translate(self, s, t):
        for vertex in self.vertices:
            vertex.x += s
            vertex.y += t
    
    def rotate(self, theta):
        theta = math.radians(theta)
        c, s = math.cos(theta), math.sin(theta)
        for vertex in self.vertices:
            x, y = vertex.x, vertex.y
            vertex.x = x * c - y * s
            vertex.y = x * s + y * c
    
    def __iter__(self):
        return SimplePoly.SimplePolyIterator(self)
    
    def __len__(self):
        return len(self.vertices)

class ConvPoly(Point):
    pass
class RegularPoly(ConvPoly):
    pass
class Triangle(ConvPoly):
    pass
class Rectangle(ConvPoly):
    pass


