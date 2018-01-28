#Write a program that examines three variables–x, y, and z 
#and prints the largest odd number among them. If none of them are odd, 
#it should print a message to that effect.

x = int( input ( "Enter x: " ) )
y = int( input ( "Enter y: " ) )
z = int( input ( "Enter z: " ) )

if x % 2 == 0 and y % 2 == 0 and z % 2 == 0:
    print ("No odd numbers")
elif x % 2 == 0 and y % 2 == 0 and z % 2 != 0:
    print ("z: ", z , " is the greatest odd number amongst", x, y, z)
elif x % 2 == 0 and y % 2 != 0 and z % 2 == 0:
    print ("y: ", y , " is the greatest odd number amongst", x, y, z)
elif x % 2 != 0 and y % 2 == 0 and z % 2 == 0:
    print ("x: ", x, " is the greatest odd number amongst", x, y, z)


elif x % 2 == 0 and y % 2 != 0 and z % 2 !=0:
    if y > z:
        print ("y:", y , "is the greatest odd number amongst", x, y, z)
    else:
        print ("z:", z , "is the greatest odd number amongst", x, y, z)
        

elif x % 2 != 0 and y % 2 != 0 and z % 2 == 0:
    if x > y:
        print ("x:", x , "is the greatest odd number amongst", x, y, z)
    else:
        print ("y:", y , "is the greatest odd number amongst", x, y, z)

elif x % 2 != 0 and y % 2 == 0 and z % 2 != 0:
    if x > z:
        print ("x:", x , "is the greatest odd number amongst", x, y, z)
    else:
        print ("z:", z , "is the greatest odd number amongst", x, y, z)

elif x % 2 != 0 and y % 2 != 0 and z %2 != 0:
    if x > y and x > z:
        print ("x:", x , "is the greatest odd number amongst", x, y, z)
    elif y > z:
        print ("y:", y , "is the greatest odd number amongst", x, y, z)
    else:
        print ("z:", z , "is the greatest odd number amongst", x, y, z)


