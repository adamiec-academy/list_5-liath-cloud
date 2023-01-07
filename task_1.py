def longest_word(words):
    longest = ""
    length = 0

    for i in range(len(words)):
        if len(words[i]) > length:
            length = len(words[i])
            longest = words[i]

    return longest
