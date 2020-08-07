def has_negatives(a):
    """
    YOUR CODE HERE
    """
    num_table = {}
    result = []

    for n in a:

        # input number into dictionary 
        num_table[n] = n
        # check to see if negative version is in dict
        # `0` doesn't have a negative version - fixes large test
        if n != 0 and -n in num_table:
            result.append(abs(n)) # abs() b/c input could give neg value first

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
