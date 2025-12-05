print("\n")


def check_invalid_simple(num: str) -> bool:
    if len(num) % 2 != 0:
        return False
    left: str = num[: len(num) // 2]
    right: str = num[len(num) // 2 :]
    # print(f"{num} - Left: {left}, Right: {right} - Equal: {left == right}")
    return left == right


def day2_part1():
    with open("2_input.txt") as f:
        cnt = 0
        for line in f:
            l = line.strip()
            ranges = l.split(",")
            for r in ranges:
                start, end = map(int, r.split("-"))
                # print(f"Range from {start} to {end}")
                for i in range(int(start), int(end) + 1):
                    if check_invalid_simple(str(i)):
                        print(i)
                        cnt += i
        print(cnt)

def check_invalid(s: str):
    ss = (s + s)[1:-1]
    idx = ss.find(s)
    if idx == -1:
        return None
    return s[:idx + 1]

def day2_part2():
    with open("2_input.txt") as f:
        cnt = 0
        for line in f:
            l = line.strip()
            ranges = l.split(",")
            for r in ranges:
                start, end = map(int, r.split("-"))
                for i in range(int(start), int(end) + 1):
                    if check_invalid(str(i)):
                        print(i)
                        cnt += i
        print(cnt)


if __name__ == "__main__":
    day2_part2()
