from vectorengine import vector
class force(vector):
    def __init__(self,x,y):
        super().__init__(x,y)

class object(vector):
    def __init__(self,x,y,mass):
        self.pos=vector(x,y)
        self.v=vector(0,0)
        self.mass=mass

    def velocity(self,t,F):
        self.v=vector((F.x/self.mass)*t,(F.y/self.mass)*t)
        self.pos=vector(self.pos.x+(self.v.x*t),self.pos.y+(self.v.y*t))
        
    def apply(self,t,F=force):
        self.velocity(t,F)

    def show(self):
        self.pos.display()
        self.v.display()
    

ob=object(0,0,1)
ob.show()
ob.apply(5,force(-2,-1))
ob.show()