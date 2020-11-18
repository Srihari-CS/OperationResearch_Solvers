import os

def string_to_intList(line):
    line = line.split(' ')
    int_list = []
    for s in line:
        int_list.append(int(s))
    return int_list

def get_input():
    path = os.getcwd()
    input_filename = path + '\\Inputs\\Trans_input.txt'
    input_file = open(input_filename, 'r')

    #Getting the no. of rows and columns

    read_line = input_file.readline()
    line = string_to_intList(read_line)
    rows, cols = line[0], line[1]

    #Supply and Demand Limits
    read_line = input_file.readline()
    supply = string_to_intList(read_line)

    read_line = input_file.readline()
    demand = string_to_intList(read_line)

    #Cost Matrix
    cost_matrix = []
    read_lines = input_file.readlines()
    for line in read_lines:
        cost_matrix.append(string_to_intList(line))

    print(cost_matrix)

def main():
    get_input()

if __name__ == '__main__':
    main()