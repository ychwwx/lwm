import math
class shapes():
    def __init__(self,a,b):
        self.a=a
        self.b=b
class ellipse(shapes):
    def area(self):
        return( self.a*self.b*math.pi)
class circle(ellipse):
    pass
    
class rectangle(shapes):
    def area(self):
        return(self.a*self.b)
class square(rectangle):
    pass
def compute_area(shapes):
    return sum(i.area() for i in shapes)

shapes=[ellipse(10,20),square(15,15),circle(5,5),rectangle(20,15),circle(5,5)
        ,square(15,15),ellipse(10,20)]
total_area=compute_area(shapes)
print('图形总面积=',total_area)  
