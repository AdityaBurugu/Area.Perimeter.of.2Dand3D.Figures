from math import sqrt
###################     CLASS RECTANGLE      ####################
class Rectangle :
    def __init__(self,length, bredth):
        self.length = length
        self.bredth = bredth

    def Area(self):
        A = self.length * self.bredth
        return A

    def Perimater(self):
        P = (self.length + self.bredth) * 2
        return P
####################################################################
################         CLASS  TRIANGLE         ###################
class Triangle :
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def Perimeter(self):
        P = self.a + self.b + self.c
        return P

    def Area(self):
        s = self.Perimeter() / 2
        A = sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return A
###################################################################
################         CLASS  CIRCLE         ###################
class Circle :
    def __init__(self,R):
        self.R = R

    def Circumference(self):
        C = 2*22/7*self.R
        return C

    def Area(self):
        A = 22/7*self.R**2
        return A
###################################################################
################         CLASS  TRAPEZIUM         ###################
class Trapezium :
    def __init__(self,Side1,Side2,Side3,Side4,Height):
        self.Side1 = Side1
        self.Side2 = Side2
        self.Side3 = Side3
        self.Side4 = Side4
        self.Height = Height
    def Perimeter(self):
        P = self.Side1+self.Side2+self.Side3+self.Side4
        return P

    def Area(self):
        A = 0.5*(self.Side1+self.Side2)*self.Height
        return A
###################################################################
################         CLASS  SQUARE         ###################
class Square:
    def __init__(self, Side):
        self.Side = Side

    def Perimeter(self):
        P = self.Side*4
        return P

    def Area(self):
        A = self.Side**2
        return A
###################################################################
################         CLASS  RHOMBUS         ###################
class Rhombus :
    def __init__(self, Side,Diagonal1,Diagonal2):
        self.Side = Side
        self.Diagonal1 = Diagonal1
        self.Diagonal2 = Diagonal2


    def Perimeter(self):
        P = self.Side*4
        return P

    def Area(self):
        A = (self.Diagonal1*self.Diagonal2)*0.5
        return A
###################################################################
################         CLASS  PARALLELOGRAM         ###################
class Parallelogram:
    def __init__(self,length, bredth):
        self.length = length
        self.bredth = bredth

    def Area(self):
        A = self.length * self.bredth
        return A

    def Perimater(self):
        P = (self.length + self.bredth) * 2
        return P
###################################################################
################         CLASS  CUBE         ###################
class Cube:
    def __init__(self,Side):
        self.Side = Side

    def Curved_Area(self):
        CA = 4*self.Side**2
        return CA

    def Total_Area(self):
        TA = 6*self.Side**2
        return TA
    def Volume(self):
        Vol = self.Side**3
        return Vol
###################################################################
################         CLASS  CUBOID         ###################
class Cuboid:
    def __init__(self,length,breadth,height):
        self.length = length
        self.breadth = breadth
        self.height = height

    def Curved_Area(self):
        CA = 2*(self.length + self.breadth)*self.height
        return CA

    def Total_Area(self):
        TA = 2*((self.length*self.breadth) + (self.breadth*self.height) + (self.height*self.length))
        return TA
    def Volume(self):
        Vol = self.length*self.breadth*self.height
        return Vol
    ###################################################################
    ################         CLASS  CYLINDER         ###################
class Cylinder:
    def __init__(self,Radius,height):
        self.Radius = Radius
        self.height = height

    def Curved_Area(self):
        CA = 2* 22/7 * self.Radius * self.height
        return CA

    def Total_Area(self):
        TA = 2*22/7*(self.Radius*(self.Radius+self.height))
        return TA

    def Volume(self):
        Vol = 22/7*self.Radius**2*self.height
        return Vol
    ###################################################################
     ################         CLASS  CONE         ###################
class Cone :
    def __init__(self, Radius,height):
        self.Radius = Radius
        self.height = height

    def Curved_Area(self):
        Slant_height = sqrt((self.Radius**2) + (self.height**2))
        print('Slant_Height =',Slant_height)
        CA = 22 / 7 * self.Radius * Slant_height
        return CA

    def Total_Area(self):
        Slant_height = sqrt((self.Radius ** 2) + (self.height ** 2))
        TA = 22 / 7 * (self.Radius * (self.Radius + Slant_height))
        return TA

    def Volume(self):
        Vol = 1 / 3 * 22 / 7 * self.Radius ** 2 * self.height
        return Vol
 ###################################################################
     ################         CLASS  FRUSTUM OF CONE         ###################
class Frustum_Cone:
    def __init__(self, Radius1,Radius2,height):
        self.Radius1 = Radius1
        self.Radius2 = Radius2
        self.height = height

    def Curved_Area(self):
        Slant_height =  Slant_height = sqrt((self.Radius1 - self.Radius2)**2 + (self.height**2))
        print('Slant_Height =',Slant_height)
        CA = 22 / 7 * (self.Radius1 + self.Radius2) * Slant_height
        return CA

    def Total_Area(self):
        Slant_height = sqrt((self.Radius1 - self.Radius2)**2 + (self.height**2))
        TA = 22 / 7 *((self.Radius1**2) + (self.Radius2**2) + (self.Radius1 + self.Radius2)*Slant_height)
        return TA

    def Volume(self):
        Vol = 1/3 * 22/7 * self.height * (self.Radius1**2 + self.Radius2**2 + (self.Radius1 * self.Radius2))
        return Vol
###################################################################
     ################         CLASS  SPHERE         ###################
class Sphere:
    def __init__(self, Radius):
        self.Radius = Radius

    def Total_Area(self):
        TA = 4 * 22/7 * self.Radius ** 2
        return TA

    def Volume(self):
        Vol = 4/3 * 22/7 * self.Radius**3
        return Vol
    ###################################################################
    ################         CLASS  HEMI_SPHERE         ###################
class H_Sphere:
    def __init__(self, Radius):
        self.Radius = Radius
    def Curved_Area(self):
        CA = 2 * 22/7 * self.Radius**2
        return CA
    def Total_Area(self):
        TA = 3 * 22 / 7 * self.Radius ** 2
        return TA

    def Volume(self):
        Vol = 2 / 3 * 22 / 7 * self.Radius ** 3
        return Vol