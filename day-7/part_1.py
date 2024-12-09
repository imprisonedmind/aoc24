from itertools import product
from utils import get_file_input


def clean_data(data):
    """Create an integer one to many store"""
    cleaned_data = []
    for line in data:
        x = line.split(":")
        clean_total = int(x[0])
        many = x[1].strip().split(" ")
        cleaned_many = [int(i) for i in many]
        cleaned_data.append([clean_total, cleaned_many])
    return cleaned_data


def build_operators_list(numbers):
    """Create all the possible operators"""
    n = len(numbers)
    if n < 2:
        return []
    return list(product(['+', '*'], repeat=n - 1))


def evaluate_left_to_right(numbers, operators, target):
    """using the relative operator eval it with Left and Right values"""
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '*':
            result *= numbers[i + 1]
    if result > target:
        pass
    return result


def create_set_of_totals(one_to_many):
    """
        Loop through our numbers and eval numbers against operators and add a matching
        total to a set
    """
    sum_totals = set()
    for numbers in one_to_many:
        total = numbers[0]
        equations = numbers[1]

        operator_combinations = build_operators_list(equations)
        for operators in operator_combinations:
            if evaluate_left_to_right(equations, operators, total) == total:
                sum_totals.add(total)

    return sum_totals


def main():
    data = get_file_input("input.txt")
    one_to_many = clean_data(data)
    sum_totals = create_set_of_totals(one_to_many)

    print("TOTAL:", sum(sum_totals))


if __name__ == '__main__':
    main()
