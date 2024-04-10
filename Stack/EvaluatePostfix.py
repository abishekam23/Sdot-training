if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        input_str = input()
        st = []
        for c in input_str:
            if c.isdigit():
                st.append(int(c))
            else:
                val1 = st.pop()
                val2 = st.pop()
                if c == '+':
                    st.append(val2 + val1)
                elif c == '-':
                    st.append(val2 - val1)
                elif c == '/':
                    st.append(val2 // val1)
                elif c == '*':
                    st.append(val2 * val1)
        print(st.pop())