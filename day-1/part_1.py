def main():
    left = []
    right = []
    total = 0

    with open('data.txt', 'r') as f:
        for line in f:
            new_line = line.split()
            num_1 = new_line[0]
            num_2 = new_line[1]
            left.append(int(num_1))
            right.append(int(num_2))

    for index, left_line in enumerate(sorted(left)):
        sorted_right = sorted(right)
        line_right = sorted_right[index]
        total += abs(left_line - line_right)
        print(left_line, "-", line_right, "=", f"{left_line - line_right}" )

    print("Total = ", total)

if __name__ == '__main__':
    main()
