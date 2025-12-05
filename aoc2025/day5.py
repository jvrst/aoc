print("\n")

def day5_part1():
    with open("5_input.txt") as f:
        ranges: list[tuple[int, int]] = []
        ingredients: set[int] = set()
        for line in f:
            l = line.strip()
            values = l.split("-")
            print(values)
            if len(values) == 2:
                start, end = values
                ranges.append((int(start), int(end)))

            if len(values) == 1 and values[0] != "":
                v = int(values[0])
                ingredients.add(v)

        valid_ingredients = set()
        for i in ingredients:
            for start, end in ranges:
                if start <= i <= end:
                    valid_ingredients.add(i)
        print(len(valid_ingredients))

def merge_intervals(intervals):
    intervals = sorted(intervals)
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))

    return merged

def day5_part2():
    with open("5_input.txt") as f:
        ranges: list[tuple[int, int]] = []

        for line in f:
            l = line.strip()
            values = l.split("-")
            if len(values) == 2:
                start, end = values
                ranges.append((int(start), int(end)))

        merged_ranges = merge_intervals(ranges)
        total_valid = 0
        for r in merged_ranges:
            print(r[1] - r[0] + 1, r)
            total_valid += r[1] - r[0] + 1 
        print("Total valid ingredients:", total_valid)


if __name__ == "__main__":
    day5_part2()

