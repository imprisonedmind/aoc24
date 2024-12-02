# Each line must be either increasing or decreasing
# Each number must follow by no more than 3 and no less than 1
def main():
    with open('data.txt', 'r') as file:
        dampened_lines = []
        distance_safe_lines = []
        total_safe_lines = []

        for index, line in enumerate(file):
            int_line = line.split()
            dampened_lines.append({index: int_line})

            # We need to make our data set larger by reproducing each line for the count
            # and removing one position
            for dampened_index, value in enumerate(int_line):
                local_line = int_line[:dampened_index] + int_line[dampened_index + 1:]
                dampened_lines.append({index: local_line})

        for dampened_line in dampened_lines:
            for key, value in dampened_line.items():
                new_line = []

                for index, num in enumerate(value):
                    curr_num = int(num)
                    prev_num = int(value[index - 1])
                    num_distance = abs(curr_num - prev_num)

                    # Make Sure the step count is safe
                    if index == 0:
                        new_line.append(curr_num)
                    else:
                        if 3 >= num_distance >= 1:
                            new_line.append(curr_num)

                if len(new_line) == len(value):
                    distance_safe_lines.append({key: new_line})

        for distance_line in distance_safe_lines:
            for key, value in distance_line.items():
                line_sorted_inc = sorted(value)
                line_sorted_dec = sorted(value, reverse=True)

                if value == line_sorted_dec:
                    total_safe_lines.append(distance_line)
                if value == line_sorted_inc:
                    total_safe_lines.append(distance_line)

        seen_keys = []
        unique_data = []
        for obj in total_safe_lines:
            for key in obj.keys():
                if key not in seen_keys:
                    seen_keys.append(key)
                    unique_data.append(obj)
                    print(obj)
                    break

    print("TOTAL SAFE:", len(unique_data))


if __name__ == '__main__':
    main()
