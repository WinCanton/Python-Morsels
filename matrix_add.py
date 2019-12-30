def matrix_add(list1, list2):
    """
        Accepts two lists-of-lists of numbers and returns one
        list-of-lists with each of the corresponding numbers in the
        two given lists-of-lists added together.

        Example:
        >>> matrix1 = [[1, -2], [-3, 4]]
        >>> matrix2 = [[2, -1], [0, -1]]
        >>> add(matrix1, matrix2)
        [[3, -3], [-3, 3]]
        >>> matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
        >>> matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
        >>> add(matrix1, matrix2)
        [[2, -1, 3], [-3, 3, -3], [5, -6, 7]]
    """
    result = []
    for each in range(len(list1)):
        inner_list  = []
        for item in range(len(list1[each])):
            inner_list.append(list1[each][item] + list2[each][item])
        result.append(inner_list)
    return result

if __name__ == "__main__":
    #matrix1 = [[1, -2], [-3, 4]]
    #matrix2 = [[2, -1], [0, -1]]
    matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
    matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
    print(matrix_add(matrix1, matrix2))
