print("\n")


def day1_part1():
    with open("1_input.txt") as f:
        cnt = 50
        cnt_zero = 0
        for line in f:
            l = line.strip()
            letter = line[0]
            nr = int(line[1:])

            nr = nr % 100
            if letter == "R" and cnt + nr > 99:
                cnt -= 100
                cnt += nr
            elif letter == "R":
                cnt += nr

            if letter == "L" and cnt - nr < 0:
                cnt += 100
                cnt -= nr
            elif letter == "L":
                cnt -= nr

            if cnt == 0:
                cnt_zero += 1
            print(letter, nr, cnt, cnt_zero)
            assert 0 <= cnt <= 99

        print(cnt_zero)


def day1_part2():
    with open("1_input.txt") as f:
        cnt = 50
        cnt_zero = 0
        for line in f:
            l = line.strip()
            letter = line[0]
            nr = int(line[1:])

            for _ in range(nr):
                if letter == "R":
                    cnt += 1
                    if cnt > 99:
                        cnt = 0
                elif letter == "L":
                    cnt -= 1
                    if cnt < 0:
                        cnt = 99

                if cnt == 0:
                    cnt_zero += 1



            print(letter,  nr, cnt, cnt_zero)
            assert 0 <= cnt <= 99

        print(cnt_zero)


if __name__ == "__main__":
    day1_part2()
