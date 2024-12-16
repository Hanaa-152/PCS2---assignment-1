def count_insertion_swaps(array):
    swaps = 0
    for current_index in range(len(array)):
        position = current_index
        while position > 0 and array[position] < array[position - 1]:
            array[position], array[position - 1] = array[position - 1], array[position]
            swaps += 1
            position -= 1
    return swaps

if __name__ == "__main__":
    file_path = '/Users/han3/Downloads/rosalind_ins-7.txt'
    with open(file_path, 'r') as file:
        file.readline()
        numbers = [int(num) for num in file.readline().strip().split(' ')]
        print(count_insertion_swaps(numbers))



