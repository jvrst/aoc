
def part_1(lines):
    most_calories = 0
    food_per_elf = []
    for line in lines:
        line = line.strip()
        if line == "":
           curr_calories = sum(food_per_elf)
           food_per_elf = []
           if curr_calories > most_calories:
               most_calories = curr_calories
        else:
            food_per_elf.append(int(line))
    return most_calories

def part_2(lines):
    food_per_elf = []
    current_elf = []
    for line in lines:
        line = line.strip()
        if line == "":
            curr_calories = sum(current_elf)
            food_per_elf.append(curr_calories)
            current_elf = []
        else:
            current_elf.append(int(line))

    food_per_elf.sort()
    print(food_per_elf[-3:])
    return sum(food_per_elf[-3:])

if __name__ == "__main__":
    f = open("./data/input_1.txt", "r")
    lines = f.readlines()
    print(part_1(lines))
    print(part_2(lines))
    f.close()
