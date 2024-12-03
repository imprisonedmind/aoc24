import re


def main():
    data_string = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    wanted_start = "mul("
    mul_start = []

    mul_disabled_start = "don't()"
    mul_enable_start = "do()"
    enable_disable = []

    i = 0
    while i < len(data_string):
        if data_string[i:i + 7] == mul_disabled_start:
            mul_disabled_index = data_string.find(mul_disabled_start, i)
            enable_disable.append({mul_disabled_index: "stop"})

        if data_string[i:i + 4] == mul_enable_start:
            mul_enable_index = data_string.find(mul_enable_start, i)
            enable_disable.append({mul_enable_index: "start"})

        if data_string[i:i + 4] == wanted_start:
            mulled_starts = data_string.find(wanted_start, i)
            mul_start.append(mulled_starts)

        i += 1

    mul_numbers = []
    for mul in mul_start:
        curr_string = data_string[mul:mul + 12]
        if ")" in curr_string:
            x = re.split(r"[(,)]", curr_string)
            if x[1].isdigit() and x[2].isdigit():
                mul_numbers.append({f"{mul}": [x[1], x[2]]})

    combined_data = enable_disable + mul_numbers
    sorted_data = sorted(combined_data, key=lambda d: int(list(d.keys())[0]))

    total = 0
    is_start = True
    for value in sorted_data:
        raw_value = next(iter(value.values()))
        if raw_value == "stop":
            is_start = False
        elif raw_value == "start":
            is_start = True

        if is_start:
            print(raw_value)
            if raw_value[0].isdigit() and raw_value[1].isdigit():
                mulled = int(raw_value[0]) * int(raw_value[1])
                total += mulled

    print("TOTAL:", total)


if __name__ == "__main__":
    main()
