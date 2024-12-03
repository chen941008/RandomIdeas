stack = []
input_list=list(input("Enter a string with brackets: ").strip())
for i in input_list:
    if i == ')':
        if(not stack):
            print("illegal")
            break
        else:
            stack.pop()
    else:
        stack.append('(')
if(not stack):
    print("legal")
else:
    print("illegal")