#from pythonds.basic.stack import Stack

def divideBy2(decNumber):
    remstack = []

    while decNumber > 0:
        rem = decNumber % 2
        remstack.append(rem)
        decNumber = decNumber // 2

    binString = ""
    while len(remstack) != 0:
        binString = binString + str(remstack.pop())

    return binString

print(divideBy2(25))



def baseConverter(decNumber,base):
    digits = "0123456789ABCDEF"

    #remstack = Stack()
    remstack = []

    while decNumber > 0:
        rem = decNumber % base
        remstack.append(rem)
        decNumber = decNumber // base

    newString = ""
    while len(remstack) != 0:
        newString = newString + digits[remstack.pop()]

    return newString

print(baseConverter(25,2))
print(baseConverter(25,16))