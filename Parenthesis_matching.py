def is_balanced_brackets(n):
    stack = []
    for i in n:
        if i == ')':
            if(not stack):
                return False
            else:
                stack.pop()
        else:
            stack.append('(')
    return True
while True:
    input_string = input("Enter a string with brackets (or 'q' to quit): ").strip()
    if input_string == 'q':
        break
    if is_balanced_brackets(input_string):
        print("legal")
    else:
        print("illegal")
