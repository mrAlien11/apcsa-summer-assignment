def hypotenuse(a,b):
    return(a**2 + b**2)**0.5

def non_hypotenuse(a, b):
    if a > b:
        return(a**2 - b**2)**0.5
    else:
        return(b**2 - a**2)**0.5

def sum(a,b):
    return 180 - (a + b)

def area(a,b):
    return (a*b)/2

def perimeter(a,b,c):
    return a+b+c

def option():
    choice = input("y to start, n to exit: ")
    if choice == "y":
        a= int(input("length of side a or 0 for unknown: "))
        b= int(input("length of side b or 0 for unknown: "))
        c = int(input("length of side c or 0 for unknown: "))

        angle_a = int(input("angle of angle a or 0 for unknown: "))
        angle_b = int(input("angle of angle b or 0 for unknown: "))
        angle_c = int(input("angle of angle c or 0 for unknown: "))
        area = 0
        perimeter = 0

        return [a,b,c,angle_a,angle_b,angle_c,area,perimeter]
    if choice == "n":
        exit()

def main():
    info = option()
    if info[3] == 0:
        angle_a = sum(info[4],info[5])
        angles = [angle_a, info[4], info[5]]
    elif info[4] == 0:
        angle_b = sum(info[3],info[5])
        angles = [info[3], angle_b, info[5]]
    elif info[5] == 0:
        angle_c = sum(info[4],info[3])
        angles = [info[3], info[4], angle_c]
    else:
        angles = [info[3], info[4], info[5]]
    if angles[0] == 90 or angles[1] == 90 or angles[2] == 90:
        if info[0] == 0:
            if angles[0] == 90:
                a = hypotenuse(info[1],info[2])
            else:
                a = non_hypotenuse(info[1],info[2])
            sides = [a, info[1], info[2]]
            squared = area(info[1],info[2])
        if info[1] == 0:
            if angles[1] == 90:
                b = hypotenuse(info[0],info[2])
            else:
                b = non_hypotenuse(info[0],info[2])
            sides = [info[0], b, info[2]]
            squared = area(info[0],info[2])
        if info[2] == 0:
            if angles[2] == 90:
                c = hypotenuse(info[0],info[1])
            else:
                c = non_hypotenuse(info[0],info[1])
            sides = [info[0], info[1], c]
            squared = area(info[0],info[1])
        print("side a: ", sides[0], "side b: ", sides[1], "side c: ", sides[2], "angle a: ", angles[0], "angle b: ", angles[1], "angle c: ", angles[2], "area: ", squared, "perimeter: ", perimeter(sides[0],sides[1],sides[2]))
    else:
        print("0 for unkown")
        print("angle a: ", angles[0], "angle b: ", angles[1], "angle c: ", angles[2], "side a: ", info[0], "side b: ", info[1], "side c: ", info[2])
    
while True:
    main()