n = input().strip()

ans = 0
stack = [0]
for i in range(1, len(n)):
    if n[i] == '(':
        stack.append(0)
    elif n[i] == ')':
        if stack[-1] == 0:
            if len(stack) >= 2:
                stack[-2] += 1
            stack.pop()
        elif stack[-1] != 0:
            if len(stack) >= 2:
                stack[-2] += stack[-1]
            ans += stack[-1] + 1
            stack.pop()
print(ans)