def unique(data):
    result = set()
    result_list = []
    for i in range(len(data)):
        if data[i] not in result:
            result_list.append(data[i])
            result.add(data[i])

    return result_list
