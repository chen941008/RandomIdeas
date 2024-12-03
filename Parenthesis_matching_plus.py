def is_balanced_brackets(s):
    """
    檢查輸入字串中的括號是否匹配，並根據等級規則驗證
    等級: () 最小, [] 中等, {} 最大
    """
    stack = []
    brackets = {
        ')': ('(', 1),  # 最小等級
        ']': ('[', 2),  # 中等等級
        '}': ('{', 3)   # 最大等級
    }
    reverse_brackets = {v[0]: (k, v[1]) for k, v in brackets.items()}
    for char in s:
        if not stack:
            last_open,last_level='{',3
        else:
            last_open, last_level = stack[-1]
        if char in '([{':  # 如果是開括號
            _, current_level = reverse_brackets[char]
            if (current_level>last_level):
                return False
            # 將開括號與其等級一起存入栈中
            else:
                stack.append((char,reverse_brackets[char][1]))
            
        elif char in ')]}':  # 如果是閉括號
            if not stack:
                return False
            # 檢查括號類型是否匹配，且等級是否符合規則
            expected_open, current_level = brackets[char]
            if last_open != expected_open or last_level > current_level:
                return False
            stack.pop()
        else:
            return False
    return len(stack) == 0

# 測試範例
while True:
    input_string = input("Enter a string with brackets (or 'q' to quit): ").strip()
    if input_string == 'q':
        break
    
    if is_balanced_brackets(input_string):
        print("legal")
    else:
        print("illegal")
