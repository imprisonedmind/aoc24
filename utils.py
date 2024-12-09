def get_file_input(file_name):
    """Converts plain_text file into an list of lists"""""
    data = []
    with open(file_name, "r") as file:
        for line in file:
            data.append(line.strip())
    return data

def write_out(file_name, data):
    """Writes of the context of a list to a file"""""
    with open(file_name, "w") as file:
        for line in data:
            file.write(line + "\n")

"""
The following are helpers for matrix's 
"""
def convert_to_matrix(data):
    """Converts a list of lists into a matrix"""
    matrix = []
    for line in data:
        x = []
        for char in line:
            x.append(char)
        matrix.append(x)
    return matrix

def convert_from_matrix_to_str_list(data):
    """Un converts a list of lists into a list of strings"""
    str_list = []
    for line in data:
        local_string = "".join(line)
        str_list.append(local_string)
    return str_list

def find_start_pos(matrix, target_char):
    """Finds the starting cords of a given char in a string matrix"""
    found_position = None
    for y, row in enumerate(matrix):
        for x, char in enumerate(row):
            if char == target_char:
                found_position = [x, y]
                break
        if found_position:
            break
    return found_position

def is_valid_position(position, matrix):
    """Checks if a position is valid in a matrix"""
    rows = len(matrix)
    cols = len(matrix[0])
    x, y = position
    return 0 <= x < rows and 0 <= y < cols

def print_matrix(matrix):
    """Prints a matrix"""
    for line in matrix:
        print(line)