def longestValidParentheses(S):
    stack = [-1]
    ans = 0
    for i in range(len(S)):
        if S[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                ans = max(ans, i - stack[-1])
    return ans

if __name__ == "__main__":
    str = input()
    print(longestValidParentheses(str))