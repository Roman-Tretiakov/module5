def all_variants(text):
    if len(text) == 1:
        yield text
    else:
        for i in range(len(text)):
            yield text[i]
        for i in range(len(text)):
            if i < len(text) - 1:
                yield text[i] + text[i + 1]
            else:
                yield text


a = all_variants("abcdefg")
for i in a:
    print(i)