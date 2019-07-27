# implement is_numeric(string) function -
#   returns True if the string is numeric, False otherwise

def is_numeric(input):
    '''
        castings = [int, float, complex,
        lambda s: int(s,2),  #binary
        lambda s: int(s,8),  #octal
        lambda s: int(s,16)] #hex
    '''
    castings = [int, float]
    for cast in castings:
        try:
            cast(input)
            return True
        except ValueError:
            pass
    return False


assert is_numeric('12') == True
assert is_numeric('-1') == True
assert is_numeric('+100') == True
assert is_numeric('') == False
assert is_numeric('1.2') == True
assert is_numeric('0.00023') == True
assert is_numeric('.00023') == True
assert is_numeric('3.3.3.3') == False
assert is_numeric('3. 3') == False