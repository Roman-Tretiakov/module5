def all_variants(text):
    _len = len(text)
    if _len == 1:
        yield text
    else:
        for i in range(_len):
            yield text[i]
        for i in range(_len - 1):
            yield text[i] + text[i + 1]
        yield text


a = all_variants("abcdefg")
for i in a:
    print(i)