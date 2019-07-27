# Python3 code to Check for
# balanced parentheses in an expression
'''
for each new opening - memorize
if closing and nothing memorized then exit it is unbalansed

'''

open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]


# Function to check parentheses
def check(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                    (open_list[pos] == stack[len(stack) - 1])):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"


# Driver code




def check2(str):
    memorize = []
    for braces in str:
        if braces not in "(){}[]":
            continue
        if braces in '([{':
            memorize.append(braces)
        else:
            if len(memorize) == 0:
                return "Unbalansed"
            left = memorize.pop()
            if left == "(":
                right = ")"
            if left == "{":
                right = "}"
            if left == "[":
                right = "]"
            if braces != right:
                return "Unbalansed"
    return "Balansed"





string = "{[A]{()}}"
print(string, "-", check2(string))

string = "[{}{})(]"
print(string, "-", check2(string))

string = "[(])"
print(string, "-", check2(string))



# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# For example, given n = 3, a solution set is:
# [ "((()))", "(()())", "(())()", "()(())", "()()()"]


def generateParenthesis(n):

    if not n: return ['']
    res = []

    def dfs(left, right, cur):
        if not left and not right:
            res.append(cur)
            return
        if left:
            dfs(left - 1, right, cur + '(')
        if left < right:
            dfs(left, right - 1, cur + ')')
        return

    dfs(n, n, '')
    return res

print generateParenthesis(3)