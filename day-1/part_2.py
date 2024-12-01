def main():
    left = []
    right = []

    with open('data.txt', 'r') as f:
        for line in f:
            new_line = line.split()
            num_1 = new_line[0]
            num_2 = new_line[1]
            left.append(int(num_1))
            right.append(int(num_2))

    # I need to check every left_line against every right_line and count the number
    # of times it appears. Then times the number by its count.
    total_similarity_count = 0
    for index, left_line in enumerate(sorted(left)):
        line_similarity_count = 0
        line_similarity_total = 0

        for right_line in sorted(right):
            if left_line == right_line:
                line_similarity_count += 1

        if line_similarity_count > 0:
            line_similarity_total += left_line * line_similarity_count
            total_similarity_count += line_similarity_total
            print("Line Similarity Count: ", left_line, "*", line_similarity_count, "---", "Line Similarity Total: ", line_similarity_total)

    print("Total Similarity Count: ", total_similarity_count)

if __name__ == '__main__':
    main()
