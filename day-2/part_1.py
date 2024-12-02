# Each line must be either increasing or decreasing
# Each number must follow by no more than 3 and no less than 1
def main():
    with open('data.txt', 'r') as file:
        distance_safe_lines = []
        total_safe_lines = []

        for line in file:
            int_line = line.split()
            new_line = []

            for index, num in enumerate(int_line):
                curr_num = int(num)
                prev_num = int(int_line[index - 1])
                num_distance = abs(curr_num - prev_num)

                # Make Sure the step count is safe
                if index == 0:
                    new_line.append(curr_num)
                else:
                    if 3 >= num_distance >= 1:
                        new_line.append(curr_num)

            if len(new_line) == len(int_line):
                distance_safe_lines.append(new_line)

        for distance_line in distance_safe_lines:
            line_sorted_inc = sorted(distance_line)
            line_sorted_dec = sorted(distance_line, reverse=True)

            if distance_line == line_sorted_dec:
                total_safe_lines.append(distance_line)
                print("DEC:", distance_line)
            if distance_line == line_sorted_inc:
                total_safe_lines.append(distance_line)
                print("INC:", distance_line)

    print("TOTAL SAFE:", len(total_safe_lines))


if __name__ == '__main__':
    main()
