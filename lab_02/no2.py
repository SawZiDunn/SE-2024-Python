import math

def main():
    radius = float(input("Radius: "))
    length = float(input("Length: "))
    
    area = math.pi * (radius ** 2)
    volume = area * length
    
    print(f"Area: {area:.2f}")
    print(f"Volume: {volume:.2f}")
    
    
main()