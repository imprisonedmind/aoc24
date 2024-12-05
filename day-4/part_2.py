from idlelib.codecontext import get_line_info


def main():
    line_arr = []

    total = []
    with open('data.txt', 'r') as file:
        data = file.readlines()
        for line in data:
            line_arr.append(line.strip())

    for i, line in enumerate(line_arr):
        for index, char in enumerate(line):
            if char == "A":
                #              X      Y
                top_l = [index - 1, i - 1]
                top_r = [index + 1, i - 1]
                bottom_l = [index - 1, i + 1]
                bottom_r = [index + 1, i + 1]

                # make sure we don't return negatives
                if (
                        is_within_bounds(top_l[0], top_l[1], line_arr) and
                        is_within_bounds(top_r[0], top_r[1], line_arr) and
                        is_within_bounds(bottom_l[0], bottom_l[1], line_arr) and
                        is_within_bounds(bottom_r[0], bottom_r[1], line_arr)
                ):

                    #                        Y         X
                    top_l_char = line_arr[top_l[1]][top_l[0]]
                    top_r_char = line_arr[top_r[1]][top_r[0]]
                    bot_l_char = line_arr[bottom_l[1]][bottom_l[0]]
                    bot_r_char = line_arr[bottom_r[1]][bottom_r[0]]

                    # if SAM SAM
                    if "S" in top_l_char and "M" in bot_r_char and "S" in top_r_char and "M" in bot_l_char:
                        joined_word = f"{top_l_char}A{bot_r_char} {top_r_char}A{bot_l_char}"
                        # print(joined_word)
                        total.append(joined_word)

                    # if SAM MAS
                    if "S" in top_l_char and "M" in bot_r_char and "M" in top_r_char and "S" in bot_l_char:
                        joined_word = f"{top_l_char}A{bot_r_char} {top_r_char}A{bot_l_char}"
                        # print(joined_word)
                        total.append(joined_word)

                    # if MAS MAS
                    if "M" in top_l_char and "S" in bot_r_char and "M" in top_r_char and "S" in bot_l_char:
                        joined_word = f"{top_l_char}A{bot_r_char} {top_r_char}A{bot_l_char}"
                        # print(joined_word)
                        total.append(joined_word)

                    # if MAS SAM
                    if "M" in top_l_char and "S" in bot_r_char and "S" in top_r_char and "M" in bot_l_char:
                        joined_word = f"{top_l_char}A{bot_r_char} {top_r_char}A{bot_l_char}"
                        # print(joined_word)
                        total.append(joined_word)

    print("TOTAL:", len(total))


def is_within_bounds(x, y, grid):
    return 0 <= y < len(grid) and 0 <= x < len(grid[y])


if __name__ == '__main__':
    main()
