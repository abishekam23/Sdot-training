def precedence(ch):
    if ch == '+' or ch == '-':
        return 1
    elif ch == '/' or ch == '*':
        return 2
    elif ch == '^':
        return 3
    else:
        return -1

if __name__ == "__main__":
    s = input()
    n = len(s)
    st = []
    ans = ""
    for i in range(n):
        c = s[i]
        if c.isalnum():
            ans += c
        elif c == '(':
            st.append(c)
        elif c == ')':
            while st and st[-1] != '(':
                ans += st.pop()
            st.pop()
        else:
            while st and precedence(st[-1]) >= precedence(c):
                ans += st.pop()
            st.append(c)
    while st:
        ans += st.pop()
    print(ans)