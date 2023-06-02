def solution(number, k):
    stack = []
    for num in number:
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)


solution("1924", 2)
solution("1231234", 3)
solution("4177252841", 4)
