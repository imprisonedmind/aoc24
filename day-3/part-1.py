import re


def main():
    # data_string = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    with open('data.txt', 'r') as file:
        data_string = file.read()
        wanted_start = "mul("
        mul_start_index = []
        mul_numbers = []
        total = 0

        i = 0
        while i < len(data_string):
            if data_string[i:i + 4] == wanted_start:
                x = data_string.find(wanted_start, i)
                mul_start_index.append(x)
            i += 1

        for mul in mul_start_index:
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
