#"Introduction to Computation and Programming Using Python: \
#With Application to Understanding Data (MIT Press) 2nd , Kindle Edition" 
#by John Guttag

#       Finger Exercise 3:
#       Replace the comment in the following code with a while loop
#       numXs = int(input('How many times should I print the letter X? '))
#       toPrint = ''
#       #concatenate X to toPrint numXs times
#       print (toPrint)

numXs = int( input("How many times should I print the letter X? ") )
toPrint = ''
if numXs < 1:
    print ("Value of numXs is less than or equal to zero")
else:
    while numXs > 0:
      toPrint = toPrint + "x"
      numXs = numXs -1
    print(toPrint)


#Another way to do it, is convert numXs to absolute value.
#numXs = int( (input("How many times should I print the letter X? ") ) )
#toPrint = ''
#if numXs == 0:
#    print ("Are you sure??")
#if numXs < 0 :
#    print ("Value of numXs is less than zero. Converting ", numXs, " to " , abs(numXs) )
#    numXs = abs(numXs)
#
#    while numXs > 0:
#      toPrint = toPrint + "x"
#      numXs = numXs -1
#    print(toPrint)

#One more way to do it is to initialize numXs to absolute value.
#numXs = abs (int( input("How many times should I print the letter X? ") ) )
#print ("Note: Negative numbers will be converted to absolute value")
#toPrint = ''
#while numXs > 0:
#    toPrint = toPrint + "x"
#    numXs = numXs -1
#print(toPrint)
#
