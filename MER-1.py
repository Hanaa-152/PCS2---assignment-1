def merge_sorted_arrays(file_path):
    with open(file_path, 'r') as file:
        n = int(file.readline().strip())
        A = list(map(int, file.readline().strip().split()))
        m = int(file.readline().strip())
        B = list(map(int, file.readline().strip().split()))

    merged_array = []
    i = 0
    j = 0

    while i < len(A) or j < len(B):
        if i < len(A) and j < len(B):
            if A[i] <= B[j]:
                merged_array.append(A[i])
                i += 1
            else:
                merged_array.append(B[j])
                j += 1
        elif i < len(A):
            merged_array.append(A[i])
            i += 1
        elif j < len(B):
            merged_array.append(B[j])
            j += 1

    return merged_array

if __name__ == "__main__":
    file_path = '/Users/han3/Downloads/rosalind_mer-4.txt'  
    result = merge_sorted_arrays(file_path)
    print(" ".join(map(str, result)))

