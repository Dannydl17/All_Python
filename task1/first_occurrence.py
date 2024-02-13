def first_occurrence(word):
    remove = word[1:]
    first = word[:1]
    con = ""
    con += first
    for words in remove:
        if first == words:
            words = '$'
        con += words
    return con
