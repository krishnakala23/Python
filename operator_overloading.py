class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __sub__(self,other):
        return point(self.x-other.x,self.y-other.y)
    def __str__(self):
        return f"({self.x},{self.y})"
p1=point(6,8)
p2=point(3,4)
print(p1-p2)
