def main():
    with open('data.txt', 'r') as file:
        line_arr = []
        horizontal_words = []
        vertical_words = []
        diagonal_words = []

        # create line arr
        for line in file:
            stripped_line = line.strip()
            line_arr.append(stripped_line)

        # check for x-axis words
        for line in line_arr:
            for index, char in enumerate(line):
                word = line[index:index + 4]
                if word == "XMAS" or word == "SAMX":
                    horizontal_words.append(word)

        rows = len(line_arr)
        cols = len(line_arr[0])

        # Check y-axis columns for word
        for col in range(cols):
            column_values = [row[col] for row in line_arr if col < len(row)]
            for index, value in enumerate(column_values):
                word = "".join(column_values[index:index + 4])
                if word == "XMAS" or word == "SAMX":
                    vertical_words.append(word)

        diagonals_ltr = []
        diagonals_rtl = []

        # check LTR diagonal
        for col in range(cols):
            diagonal = []
            x, y = 0, col
            while x < rows and y < cols:
                diagonal.append(line_arr[x][y])
                x += 1
                y += 1
            diagonals_ltr.append(''.join(diagonal))

        for row in range(1, rows):
            diagonal = []
            x, y = row, 0
            while x < rows and y < cols:
                diagonal.append(line_arr[x][y])
                x += 1
                y += 1
            diagonals_ltr.append(''.join(diagonal))

        # check RTL diagonal
        for col in range(cols):
            diagonal = []
            x, y = 0, col
            while x < rows and y >= 0:
                diagonal.append(line_arr[x][y])
                x += 1
                y -= 1
            diagonals_rtl.append(''.join(diagonal))

        for row in range(1, rows):
            diagonal = []
            x, y = row, cols - 1
            while x < rows and y >= 0:
                diagonal.append(line_arr[x][y])
                x += 1
                y -= 1
            diagonals_rtl.append(''.join(diagonal))

        combined_diagonals = diagonals_ltr + diagonals_rtl
        for lines in combined_diagonals:
            for index, char in enumerate(lines):
                word = lines[index:index + 4]
                if word == "XMAS" or word == "SAMX":
                    diagonal_words.append("SAMX")

        print(horizontal_words)
        print(vertical_words)
        print(diagonal_words)

        total_words = horizontal_words + vertical_words + diagonal_words
        print("TOTAL WORDS: ", len(total_words))


if __name__ == '__main__':
    main()
