def longest_word():

    data = []

    for line in open("words.txt", encoding="utf-8"):
        data.append(line.strip('/n'))

    length = 0
    longest = ''

    for i in range(len(data)):
        if len(data[i]) > length:
            length = len(data[i])
            longest = data[i]

    return longest
