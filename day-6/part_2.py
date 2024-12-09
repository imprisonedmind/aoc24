from utils import is_valid_position, get_file_input, convert_to_matrix, find_start_pos, \
    write_out, convert_from_matrix_to_str_list

def move_player(start_pos, matrix, numer_set):
    #              NORTH    EAST    SOUTH    WEST
    #              X   Y    X  Y    X  Y    X   Y
    directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]
    directions_char = ["N", "E", "S", "W"]
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
        matrix[pos[1]][pos[0]] = directions_char[pointer % len(directions_char)]
        next_pos_char = matrix[next_pos[1]][next_pos[0]]

def write_to_file(matrix):
    data = convert_from_matrix_to_str_list(matrix)
    write_out("output.txt", data)


def main():
    data = get_file_input("demo.txt")
    matrix = convert_to_matrix(data)

    starting_pos = find_start_pos(matrix, "^")
    number_set = set()
    move_player(starting_pos, matrix, number_set)

    write_to_file(matrix)
    # write_out("output.txt", matrix)
    # print("TOTAL:", len(number_set))


if __name__ == '__main__':
    main()
