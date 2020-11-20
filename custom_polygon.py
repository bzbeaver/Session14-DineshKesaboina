from polygon import Polygon

class CustomPolygon:
    """
  A class that produces polygons of all sizes greater than 0 and less than 25.
  ...
  Attributes
  ---------
  max_edges : int
    Maxium number of edges or vertices in a polygon sequence
  common_circum_rad : int
    Length of the common circumradius of the sequence of polygons
  
  Properties
  ---------
  max_efficiency : float
    Highest ratio of Area to Perimeter in a polygon sequence
  """
    def __init__(self, max_edges, common_circum_rad):
      assert max_edges > 0 and max_edges <= 25, "Maximum number of edges can only be in the range 1 to 25!"

      self.max_edges =  max_edges
      self.common_circum_rad = common_circum_rad

      self.polygons = [Polygon(i, common_circum_rad) for i in range(1, max_edges+1)]

    def __iter__(self):
        return self.CustomPolygonIterator(self.max_edges, self.common_circum_rad)

    @property
    def max_efficiency(self):
      all_ratios = list(map(lambda x:(x.area/x.perimeter), self.polygons))
      return str(max(self.polygons, key = lambda x:(x.area/x.perimeter))) +  f' and area to perimeter ratio of {max(all_ratios)}'

    def __getitem__(self, index):
      if isinstance(index, int):
          return self.polygons[index]

    def __len__(self):
      return len(self.polygons)
    
    def __reversed__(self):
        return self.CustomPolygonIterator(self.max_edges, self.common_circum_rad, reverse=True)
    
    def __repr__(self):
      return f"Polygon sequence with {self.__len__()} polygons with a circumradius of {self.common_circum_rad}"

    class CustomPolygonIterator:
      def __init__(self, max_edges, common_circum_rad, *, reverse=False):
          self.max_edges =  max_edges
          self.reverse = reverse
          self.i = 0
          self.common_circum_rad = common_circum_rad
          
      def __iter__(self):
          return self
      
      def __next__(self):
          if self.i >= self.max_edges:
              raise StopIteration
          else:
              if self.reverse:
                  index = self.length -1 - self.i
              else:
                  index = self.i
              self.i += 1
              return Polygon(self.i, self.common_circum_rad)