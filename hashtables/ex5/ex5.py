def finder(files, queries):
    """
    YOUR CODE HERE
    """
    result = []
    directory = {}

    # build file directory
    # key = file_name: value = file path
    for f in files:
        path = f.split("/")
        # return(path)
        file_name = path[-1]
        
        if file_name not in directory:
            directory[file_name] = []

        directory[file_name].append(f)

    # check directory for query strings
    for q in queries:
        if q in directory:
            result.extend(directory[q])

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
