import math

print("*****Volume of the Cube*****\n")
side=float(input("Enter the edge of the cube "))
volume = side**3
print("Volume of the cube of side = ",side," is " ,volume,)

print("\n*****Volume of Cuboid*****\n")
length=float(input("Enter the length of the cuboid "))
breadth=float(input("Enter the breadth of the cuboid "))
height=float(input("Enter the height of the cuboid "))
volume=length * breadth * height
print("Volume of the cuboid of length = ",length,", breadth = ",breadth,", height = ",height," is " ,volume)

print("\n*****Volume of cone*****\n")
radius = float(input("Enter the radius of the cone "))
height = float(input("Enter the height of the cone "))
volume = round((((math.pi)*(radius**2)*height)/3),2)
print("Volume of cone of radius = ",radius,", height = ", height, " is ", volume)

print("\n*****Volume of right circular cone*****\n")
radius = float(input("Enter the radius of the right circular cone "))
height = float(input("Enter the height of the right circular cone "))
volume = round((((math.pi)*(radius**2)*height)/3),2)
print("Volume of right circular cone of radius = ",radius,", height = ", height, " is ", volume)

print("\n*****Volume of a prism*****\n")
base_length = float(input("Enter the length of the base "))
base_breadth = float(input("Enter the breadth of the base "))
height = float(input("Enter the height of the prism"))
base_area = base_length * base_breadth
volume = base_area * height
print("Volume of prism of base area =",base_area,", height = ",height, " is ",volume)

print("\n*****Volume of different types of pyramid*****\n")
apothem = float(input("Enter the apothem length of the pyramid "))
base = float(input("Enter the base length of the pyramid "))
height = float(input("Enter the height of the pyramid "))
volume_square = ((base**2)*height)/3
volume_triangle = (apothem * base * height)/6
volume_pentagon = (5 * apothem * base * height)/6
volume_hexagon = apothem * base * height

print("\nVolume of a square pyramid of base = ",base,", height = ",height, " is ", volume_square)
print("Volume of a triangular pyramid of apothem = ", apothem, ", base = ",base,", height = ",height, " is ", volume_triangle)
print("Volume of a pentagonal pyramid of apothem = ", apothem, ", base = ",base,", height = ",height, " is ", volume_pentagon)
print("Volume of a hexagonal pyramid of apothem = ", apothem, ", base = ",base,", height = ",height, " is ", volume_hexagon)

print("\n*****Volume of Sphere*****\n")
radius = float(input("Enter the radius of the sphere "))
volume = round((4 * (math.pi) * (radius**3))/3)
print("Volume of the sphere of radius = ",radius," is ",volume)

print("\n*****Volume of circular cylinder*****\n")
radius = float(input("Enter the radius of the circular cylinder "))
height = float(input("Enter the height of the circular cylinder "))
volume = round((math.pi) * (radius**2) * height)
print("Volume of the circular cylinder of radius = ",radius,", height = ",height," is ",volume)