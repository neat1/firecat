import sys

data = sys.stdin.readlines()
input_list = []

for line in data:
    input_list.append(int(line.rstrip()))

printed_lines = input_list[0]
counter = 0


def extract_input(input_list, counter):
    numbers_to_check = input_list[1:]
    for i in numbers_to_check:
        check_number(i)
        counter += 1
    return counter


def check_number(number):
    if int(number) % 2 == 0:
        print(str(number) + " is even")
    else:
        print(str(number) + " is odd")


# checks the number of iteration equality with the expected number of input
def test(counter, printed_lines):
    if counter != printed_lines:
        print("Iteration failed")
        sys.exit()


counter = extract_input(input_list, counter)
test(counter, printed_lines)