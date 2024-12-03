import re


def main():
    with open('data.txt', 'r') as file:
        data_string = file.read()
        wanted_start = "mul("
        mul_start = []
        mul_numbers = []
        total = 0

        i = 0
        while i < len(data_string):
            if data_string[i:i + 4] == wanted_start:
                x = data_string.find(wanted_start, i)
                mul_start.append(x)
            i += 1

        for mul in mul_start:
            curr_string = data_string[mul:mul + 12]
            if ")" in curr_string:
                x = re.split(r"[(,)]", curr_string)
                if x[1].isdigit() and x[2].isdigit():
                    mul_numbers.append([x[1], x[2]])

        for number in mul_numbers:
            print(number)
            mulled = int(number[0]) * int(number[1])
            total += mulled

        print("TOTAL:", total)


if __name__ == "__main__":
    main()
