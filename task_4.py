def reversed_words():

    results = []
    data = []

    for line in open("words.txt", encoding="utf-8"):
        data.append(line.strip('\n'))

    data = sorted(data)
    data_krotka = set(data)

    for i in range(len(data)):
        data_inverse = data[i][::-1]
        if data_inverse in data_krotka and data_inverse != data[i]:
            results.append((data[i], data_inverse))
            data_krotka.remove(data_inverse)

    results = sorted(results)
    return results
