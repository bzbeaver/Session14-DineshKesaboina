import math

class Polygon:
    def __init__(self, n, R):

        self._n = n
        self._R = R
        self._area = None
        self._side_length = None
        self._apothem = None
        self._perimeter = None
    
    def __repr__(self):
        return f'Polygon(n={self._n}, R={self._R})'
    
    @property
    def count_vertices(self):
        return self._n
    
    @property
    def count_edges(self):
        return self._n

    @property
    def circumradius(self):
        return self._R

    @property
    def interior_angle(self):
        return (self._n - 2) * 180 / self._n

    @property
    def side_length(self):
        if self._side_length is None:
            # print('Calculating...')
            self._side_length = 2 * self._R * math.sin(math.pi / self._n)
        # print("Called")
        return self._side_length

    @property
    def apothem(self):
        if self._apothem is None:
            # print('Calculating...')
            self._apothem = self._R * math.cos(math.pi / self._n)
        # print("Called")
        return self._apothem

    @property
    def area(self):
        if self._area is None:
            # print('Calculating...')
            self._area = self._n / 2 * self.side_length * self.apothem
        # print('Called')
        return self._area

    @property
    def perimeter(self):
        if self._perimeter is None:
            # print('Calculating...')
            self._perimeter = self._n * self.side_length
        # print("Called")
        return self._perimeter

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.count_edges == other.count_edges 
                    and self.circumradius == other.circumradius)
        else:
            return NotImplemented
        
    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.count_vertices > other.count_vertices
        else:
            return NotImplemented