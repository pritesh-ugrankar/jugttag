#Write a program that examines three variables–x, y, and z 
#and prints the largest odd number among them. If none of them are odd, 
#it should print a message to that effect.

x = int( input ( "Enter x: " ) )
y = int( input ( "Enter y: " ) )
z = int( input ( "Enter z: " ) )

if x > y and x > z and x % 2 != 0:
    print ("x:", x , "is the greatest odd number amongst", x, y, z)
elif y > z and y % 2 != 0:
    print ("y:", y , "is the greatest odd number amongst", x, y, z)
elif z % 2 != 0:
    print ("z:", z , "is the greatest odd number amongst", x, y, z)
else:
    print ("No odd numbers")


####################################################################
#Here's the output of the script above.

#Here, it works fine.
#pritesh@thinkpad:~/jguttag$ python3 buggy_finger_ex2_largest_odd.py 
#Enter x: -9
#Enter y: -7
#Enter z: 7
#z: 7 is the greatest odd number amongst -9 -7 7
#
#Here the answer is wrong!! -7 and -5 are odd numbers.
#pritesh@thinkpad:~/jguttag$ python3 buggy_finger_ex2_largest_odd.py 
#Enter x: -7
#Enter y: -5
#Enter z: 2
#No odd numbers
