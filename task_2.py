def unique(data):
    result = []
    for i in range(len(data)):
        if data[i] not in result:
            result.append(data[i])

    return result
