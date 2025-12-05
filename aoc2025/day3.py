print("\n")

def max_subseq(s: str, k: int) -> str:
    st = []
    r = len(s) - k
    for c in s:
        while r and st and st[-1] < c:
            st.pop()
            r -= 1
        st.append(c)
    return "".join(st[:k])

def day3_part1():
    with open("3_input.txt") as f:
        t = 0
        for line in f:
            l = line.strip()
            b = list(l)
            c = []
            for i in range(len(b)):
                for j in range(len(b)):
                    if i < j:
                        c.append(b[i] + b[j])
            t += int(max(c))
        print(f"Total joltage: {t}")

def day3_part2():
    with open("3_input.txt") as f:
        t = 0
        for line in f:
            l = line.strip()
            bank_joltage = int(max_subseq(l, 12))
            t += bank_joltage
        print(f"Total joltage: {t}")

if __name__ == "__main__":
    day3_part2()

