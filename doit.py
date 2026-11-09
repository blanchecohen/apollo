def isEven(number): 
    return number % 2 == 0

def isOdd(number): 
    return not isEven(number)

# main program
if isEven(10):
     print('Even!')
else:
     print('Odd!')

