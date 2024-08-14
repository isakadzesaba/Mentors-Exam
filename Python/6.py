def pig_latin(txt):
    word = txt.split()
    result = []

    for i in word:
        if i.isalpha():
            pig_latin_word = i[1:] + i[0] + "ay"
        else:
            prefix = i[:-1]
            suffix = i[-1]
            if prefix.isalpha():
                pig_latin_word = prefix[1:] + prefix[0] + "ay" + suffix
            else:
                pig_latin_word = i
        result.append(pig_latin_word)
    return " ".join(result)

print(pig_latin("Cucullus non facit monachum"))