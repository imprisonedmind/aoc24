from utils import is_valid_position, print_matrix, get_file_input, convert_to_matrix, \
    find_start_pos

def move_player(start_pos, matrix, numer_set):
    #                UP     RIGHT   DOWN     LEFT
    #              X   Y    X  Y    X  Y    X   Y
    directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    pointer = 0

    x_axis = start_pos[0]
    y_axis = start_pos[1]
    pos = [x_axis, y_axis]

    while True:
        direction = directions[pointer % len(directions)]

        next_pos = [pos[0] + direction[0], pos[1] + direction[1]]
        if not is_valid_position(next_pos, matrix):
            break

        next_hurdle = matrix[next_pos[1]][next_pos[0]]

        if next_hurdle == "#":
            pointer += 1
            continue

        pos = next_pos
        numer_set.add(tuple(pos))

        pos_char = matrix[pos[1]][pos[0]]
        matrix[pos[1]][pos[0]] = "H"
        next_pos_char = matrix[next_pos[1]][next_pos[0]]
        print("-----------------------")
        print_matrix(matrix)
        print(start_pos, pos, next_pos, pointer, direction, pos_char, next_pos_char)


def main():
    data = get_file_input("input.txt")
    matrix = convert_to_matrix(data)

    starting_pos = find_start_pos(matrix, "^")
    number_set = set()
    move_player(starting_pos, matrix, number_set)

    print("TOTAL:", len(number_set))


if __name__ == '__main__':
    main()
