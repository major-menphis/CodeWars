def to_camel_case(string):
    if '-' in string:
        string = string.replace('-', '_')
    words = string.split('_')
    title = words[0].istitle()
    if title:
        words = [word.capitalize() for word in words]
        result = ''.join(words)
    else:
        words2 = [words[word].capitalize() for word in range(1, len(words))]
        result = words[0] + ''.join(words2)
    return result
