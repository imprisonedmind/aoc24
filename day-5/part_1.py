def main():
    rules = []
    patterns = []
    pattern_pairs = []
    to_delete = []

    # Create our rules array
    with open('input_1.txt', 'r') as file:
        for line in file:
            new_line = line.strip().split("|")
            rules.append(new_line)

    # sanitize patterns
    with open('input_2.txt', 'r') as file:
        for line in file:
            new_line = line.strip().split(",")
            patterns.append(new_line)

    # find pairs
    for pattern_index, pattern in enumerate(patterns):
        pattern_pair = []
        for index, num in enumerate(pattern):
            i = 0
            while i < len(pattern):
                num_1 = [index, num]
                num_2 = [i, pattern[i]]
                pattern_pair.append([num_1, num_2])
                i += 1
        pattern_pairs.append(pattern_pair)

    # Check the rules for pattern matches
    for index, rule in enumerate(rules):
        for pattern_index, pattern in enumerate(pattern_pairs):
            for pair in pattern:
                rule_0, rule_1 = rule
                pair_0, pair_1 = pair[0][1], pair[1][1]
                pair_0_index, pair_1_index = pair[0][0], pair[1][0]

                # Check if rule matches in normal order
                if rule_0 == pair_0 and rule_1 == pair_1 and pair_0_index >= pair_1_index:
                    to_delete.append(pattern_index)

                # Check if rule matches in reversed order
                elif rule_0 == pair_1 and rule_1 == pair_0 and pair_0_index <= pair_1_index:
                    to_delete.append(pattern_index)

    # Remove patterns dupes after processing
    to_delete = sorted(set(to_delete), reverse=True)
    for index in to_delete:
        del patterns[index]

    # Find mids
    middle_numbers = []
    for pattern in patterns:
        middle_index = len(pattern) // 2
        middle_numbers.append(int(pattern[middle_index]))

    # Do total
    total = 0
    for number in middle_numbers:
        total += number

    print("TOTAL:", total)



if __name__ == "__main__":
    main()
