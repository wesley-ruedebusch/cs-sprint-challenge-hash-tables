def intersection(arrays):
    """
    YOUR CODE HERE
    """
    result = []
    table = {}
    length = len(arrays)
    
    # handle case, where a list has duplicates by removing them in each list
    for array in range(length):
        # print(array)
        arrays[array] = list(dict.fromkeys(arrays[array]))

    for i in arrays:
        for j in i:
            if j not in table:
                table[j] = 0
            table[j] += 1
            # table[j] = list(table[j]).insert(i, True)

    for x in table:
        if table[x] >= length:
            result.append(x)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [2, 3]) # moved 1 down
    arrays.append(list(range(2000000, 3000000)) + [1, 1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
