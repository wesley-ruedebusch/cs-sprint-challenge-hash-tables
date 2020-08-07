def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # TODO: find 2 items whose sum equals `limit`
    # return a tuple of integers of the form `(zero, one)`
    # higher value in the [0] position

    # From Hints:
    # store weight as key?
    # store weight index as value?
    # check to see if table has `limit-weight'
    
    cache = {}
    length = len(weights)
    for i in range(length):
        cache[weights[i]] = i
    for w in range(length):
        weight_diff = limit - weights[w]
        
        if weight_diff in cache:
            higher = max(w, cache[weight_diff])
            # print("h", higher)
            lower = min(w, cache[weight_diff])
            # print("l", lower)
            return(higher, lower)

    return None


weights = [4, 6, 10, 15, 16]
print(get_indices_of_item_weights(weights, 5, 21))
