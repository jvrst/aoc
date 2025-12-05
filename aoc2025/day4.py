print("\n")

def find_neighbors_count(array: list[list[int]], i: int, j: int) -> int:
    C = array[i][j]
    NW = array[i-1][j-1]
    N = array[i-1][j]
    NE = array[i-1][j+1]

    W = array[i][j-1]
    E = array[i][j+1]

    SW = array[i+1][j-1]
    S = array[i+1][j]
    SE = array[i+1][j+1]
    matches = [NW, N, NE, W, E, SW, S, SE]
    # print(i, j, matches, sum(matches), C)
    return sum(matches)

def print_board(board: list[list[int]]):
    for row in board:
        print("".join(f"{x:0}" for x in row))


def day4_part1():
    with open("4_input.txt") as f:
        count = 0
        board: list[list[int]] = []
        for line in f:
            l = line.strip()
            row = [int(c == "@") for c in l]
            row.insert(0, 0)
            row.append(0)
            board.append(row)

        zero_row = [0 for _ in range(len(board[0]))]
        board.insert(0, zero_row)
        board.append(zero_row)
        print_board(board)
        print("\n")

        for i in range(1, len(board) - 1):
            for j in range(1, len(board[i]) - 1):
                if board[i][j] == 0:
                    continue
                nb = int(find_neighbors_count(board, i, j) < 4)
                print(nb)
                count += nb
        print(count)


def day4_part2():
    with open("4_input.txt") as f:
        board: list[list[int]] = []
        for line in f:
            l = line.strip()
            row = [int(c == "@") for c in l]
            row.insert(0, 0)
            row.append(0)
            board.append(row)

        zero_row = [0 for _ in range(len(board[0]))]
        board.insert(0, zero_row)
        board.append(zero_row)

        total_removed = 0
        removables: set[tuple[int, int]] = set()
        while True:
            # print_board(board)
            # print("\n")
            for i in range(1, len(board) - 1):
                for j in range(1, len(board[i]) - 1):
                    if board[i][j] == 0:
                        continue
                    nb = find_neighbors_count(board, i, j)
                    if nb < 4:
                        removables.add((i, j))

            print(removables)
            for i, j in removables:
                board[i][j] = 0
            total_removed += len(removables)
            if len(removables) == 0:
                break
            removables.clear()

        print(total_removed)


if __name__ == "__main__":
    day4_part2()

