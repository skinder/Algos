# summ 2,3,+


def calculate(to_cal):
    ops = "+-/*"
    stack =[]
    for i in to_cal:
        if i in ops and len(stack) >= 2:
            x = stack.pop()
            y = stack.pop()
            calc = str(eval(y + i + x))
            #print calc
            stack.append(calc)
        else:
            stack.append(i)
    return stack




print calculate("632212+*-*/")


