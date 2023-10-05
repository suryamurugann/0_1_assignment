
class Point:

        def __init__(self,x,y,z):
            self.x = x
            self.y = y
            self.z = z

        def sqSum(self):
            self.x **=2
            self.y **=2
            self.z **=2
            return (self.x+self.y+self.z)

x = int(input("Enter 1st x :"))
y = int(input("Enter 1st y :"))
z = int(input("Enter 1st z :"))
obj= Point(x,y,z)
res=obj.sqSum()
print(res)
