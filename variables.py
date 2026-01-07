name="abdunabi"
age=22
is_studen=False
print("Name:",name)
print("Age:",age)
print("Is student:",is_studen)

# mathematical operations
import math

#Square
side=int(input("Enter side of square: "))
print("Square area: ",side**2)
print("Square perimeter: ",4*side)
print("-------------------------------------------------------------")


#Rectangle
length=int(input("Enter length: "))
width=int(input("Enter width: "))
print("Rectangle area:",length*width)
print("Rectangle perimeter:",2*(length+width))
print("-----------------------------------------------------------------")

#Triangle
a=int(input("Enter side a:"))
b=int(input("Enter side b:"))
c=int(input("Enter side c:"))
height=(a+b+c)/2
print("Triangle area: ",a*height/2)
print("Triangle perimeter: ",(a+b+c))
print("----------------------------------------------------------------")

#Circle
radius=int(input("Enter radius: "))
print("Circle diameter:",2*radius)
print("Circle area:",math.pi*radius**2)
print("--------------------------------------------------------------------")

#Cube
edge=int(input("Enter cube edge: "))
print("Cube volume:",edge**3)
print("Cube area:",6*edge**2)
print("--------------------------------------------------------------------")

# Rectangular Parallelepiped
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
print("Parallelepiped volume:",a*b*c)
print("Parallelepiped surface area:",2*(a*b+b*c+a*c))
